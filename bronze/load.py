from model import Base, BronzeRow
import pandas as pd
import sqlalchemy as db

def load_bronze(engine):
    Base.metadata.create_all(engine)
    df = pd.read_csv("bronza.csv", low_memory=False)
    with engine.connect() as conn:
        if db.inspect(engine).has_table("bronze_layer"):
            conn.execute(db.text("TRUNCATE TABLE bronze_layer CASCADE"))
            conn.commit()
    df = df.rename(columns={"Unnamed: 0": "id"})
    df = df.rename(columns={"name": "name_constructor"})
    df = df.rename(columns={"name_x": "name_race"})
    df = df.rename(columns={"name_y": "name_circuit"})
    df.to_sql("bronze_layer", engine, if_exists="append", index=False)
    return df