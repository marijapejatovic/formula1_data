from load import load_bronze
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
if __name__=="__main__":

    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    bronza_csv=os.getenv("bronze_csv")
    df = load_bronze(engine, bronza_csv)
