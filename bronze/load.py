from model import Base, BronzeRow
import pandas as pd
import sqlalchemy as db

def load_bronze(engine):
    Base.metadata.create_all(engine)
    df = pd.read_csv("dataEngineeringDataset.csv", low_memory=False)
    with engine.connect() as conn:
        if db.inspect(engine).has_table("bronze_row"):
            conn.execute(db.text("TRUNCATE TABLE bronze_row CASCADE"))
            conn.commit()
    df = df.rename(columns={"Unnamed: 0": "id"})
    df.to_sql("bronze_row", engine, if_exists="append", index=False)
    return df