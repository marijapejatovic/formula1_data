from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    return create_engine(os.getenv("DATABASE_URL"))

def run_bronze():
    from bronze.load import load_bronze
    engine = get_engine()
    df = load_bronze(engine)
    print(f"Bronze učitano: {len(df)} redova")

def run_silver():
    from silver.load import load_silver
    engine = get_engine()
    df = load_silver(engine)
    print(f"Silver redovi: {len(df)}")

def run_gold():
    from gold.load import load_gold
    engine = get_engine()
    load_gold(engine)
    print("Gold layer učitan")

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

    bronze_task >> silver_task >> gold_task