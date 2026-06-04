
from load import load_gold
from model import Base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from gold_checks import run_checks

if __name__ == "__main__":
    load_dotenv()
    engine = create_engine(os.getenv("DATABASE_URL"))
    Base.metadata.create_all(engine)
    print("Loading golden_row")
    load_gold(engine)
    run_checks(engine)