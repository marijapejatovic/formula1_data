from model import Base, BronzeRow
import pandas as pd

def load_bronze(engine):
    Base.metadata.create_all(engine)
    df = pd.read_csv("dataEngineeringDataset.csv", low_memory=False)
    df.to_sql("bronze_row", engine, if_exists="replace", index=False)
    return df