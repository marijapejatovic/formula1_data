from load import load_silver
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from silver_checks import run_checks

if __name__=="__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))

    df = load_silver(engine)
    run_checks(engine)
