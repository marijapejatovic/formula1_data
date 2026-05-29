from load import load_bronze
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
if __name__=="__main__":

    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = load_bronze(engine)
    pd.set_option('display.max_seq_items', None)
    print(f"Bronze učitano: {len(df)} redova")
    distinct_values = df["time_races"].dropna().unique()

    cols = ["fp1_date", "fp1_time", "fp2_date", "fp2_time", "fp3_date", "fp3_time", "quali_date", "quali_time", "sprint_date", "sprint_time"]

for col in cols:
    count = (df[col] != "\\N").sum()
    print(f"{col}: {count}")
