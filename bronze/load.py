from model import Base, BronzeRow
import pandas as pd
import sqlalchemy as db
import os

def load_bronze(engine, bronza_csv):
    Base.metadata.create_all(engine)
    df = pd.read_csv(bronza_csv, low_memory=False)
    with engine.begin() as conn:
        if db.inspect(engine).has_table("bronze_layer"):
            conn.execute(db.text("TRUNCATE TABLE bronze_layer CASCADE"))
    df = df.rename(columns={"Unnamed: 0": "id"})
    print(db.__version__)
    print(type(conn))
    print(hasattr(conn, "commit"))
    
    df.to_sql("bronze_layer", engine, if_exists="append", index=False)
    return df