from load import (
    load_dim_race,
    load_dim_driver,
    load_dim_date,
    load_dim_status,
    load_dim_constructors,
    load_dim_circuit,
    load_dim_constructorstandings,
    load_fact,
    load_fact_lap,
    load_fact_lappitstops
)
from load import load_gold

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    engine = create_engine(os.getenv("DATABASE_URL"))
    
    print("Loading dim_status")
    load_dim_status(engine)
    print("Loading dim_constructors")
    load_dim_constructors(engine)
    print("Loading dim_driver")
    load_dim_driver(engine)
    print("Loading dim_race")
    load_dim_race(engine)
    print("Loading dim_circuit")
    load_dim_circuit(engine)
    print("Loading dim_constructorstandings")
    load_dim_constructorstandings(engine)
    print("Loading dim_date")
    load_dim_date(engine)
    print("Loading fact")
    load_fact(engine)
    print("Loading fact_lap")
    load_fact_lap(engine)
    print("Loading fact_lappitstops")
    load_fact_lappitstops(engine)
    print("Loading golden_row")
    load_gold(engine)