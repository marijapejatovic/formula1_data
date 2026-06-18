from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    return create_engine(os.getenv("DATABASE_URL"))

def run_bronze():
    import sys
    sys.path.insert(0, "/opt/airflow/project/bronze")
    from load import load_bronze
    engine = get_engine()
    bronza_csv = os.getenv("bronze_csv")
    df = load_bronze(engine, bronza_csv)
    print(f"Bronze učitano: {len(df)} redova")

def run_silver():
    import sys
    sys.path.insert(0, "/opt/airflow/project/silver")
    from load import load_silver
    engine = get_engine()
    df = load_silver(engine)
    print(f"Silver redovi: {len(df)}")

def run_gold():
    import sys
    sys.path.insert(0, "/opt/airflow/project/gold")
    from load import load_gold
    engine = get_engine()
    load_gold(engine)
    print("Gold layer učitan")

def run_kafka():
    import sys
    sys.path.insert(0, "/opt/airflow/project/kafka")
    from consumer import load_kafka
    engine = get_engine()
    load_kafka(engine)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="f1_medallion_pipeline",
    default_args=default_args,
    description="F1 data pipeline: Bronze -> Silver -> Gold",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["f1", "medallion"],
) as dag:

    bronze_task = PythonOperator(
        task_id="load_bronze",
        python_callable=run_bronze,
    )

    silver_task = PythonOperator(
        task_id="load_silver",
        python_callable=run_silver,
    )

    gold_task = PythonOperator(
        task_id="load_gold",
        python_callable=run_gold,
    )

    kafka_task = PythonOperator(
        task_id="load_kafka",
        python_callable=run_kafka,
    )

    kafka_task >> bronze_task >> silver_task >> gold_task