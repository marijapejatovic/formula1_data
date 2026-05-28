from load import load_silver
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))

    df = load_silver(engine)

    print(f"Silver redovi: {len(df)}")
    print("Null vrijednosti po kolonama:")
    print(df.isnull().sum())
    print("Tipovi podataka po kolonama:")
    print(df.dtypes)