import pandas as pd
from sqlalchemy import create_engine, text
import sqlalchemy as db
import os
from dotenv import load_dotenv
from model import Base

load_dotenv()

def load_dim_race(engine):
    dimRace=pd.read_sql("select distinct \"raceId\", \"year\", \"round\", \"date\", \"race_name\", \"race_url\", \"quali_date\", \"quali_time\", \"races_time\", \"sprint_date\", \"sprint_time\", \"fp1_date\", \"fp1_time\", \"fp2_date\", \"fp2_time\", \"fp3_date\", \"fp3_time\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimRace" CASCADE'))
        conn.commit()
    dimRace.to_sql("dimRace", engine, if_exists="append", index=False)
    return dimRace
def load_dim_driver(engine):
    dimDriver=pd.read_sql("select distinct \"driverId\", \"driverRef\", \"number\", \"code\", \"forename\", \"surname\", \"nationality\", \"driver_url\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDriver" CASCADE'))
        conn.commit()
    dimDriver.to_sql("dimDriver", engine, if_exists="append", index=False)
    return dimDriver


def load_dim_date(engine):
    dates = pd.date_range(start="2012-01-01", end="2023-12-31", freq="D")
    dimDate = pd.DataFrame({
        "dateId": dates.strftime("%Y%m%d").astype(int),
        "date":   dates.date,
        "year":   dates.year,
        "month":  dates.month,
        "day":    dates.day
    })
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDate" CASCADE'))
        conn.commit()
    dimDate.to_sql("dimDate", engine, if_exists="append", index=False)
    return dimDate

def load_dim_status(engine):
    dimStatus=pd.read_sql("select distinct \"statusId\", \"status\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimStatus" CASCADE'))
        conn.commit()
    dimStatus.to_sql("dimStatus", engine, if_exists="append", index=False)
    return dimStatus

def load_dim_constructors(engine):
    dimConstructors=pd.read_sql("select distinct \"constructorId\", \"constructorRef\", \"constructor_name\", \"constructor_nationality\", \"constructor_url\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimConstructors" CASCADE'))
        conn.commit()
    dimConstructors.to_sql("dimConstructors", engine, if_exists="append", index=False)
    return dimConstructors

def load_dim_circuit(engine):
    dimCircuit=pd.read_sql("select distinct \"circuitId\", \"circuitRef\", \"circuit_name\", \"location\", \"country\", \"lat\", \"lng\", \"alt\", \"circuit_url\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimCircuit" CASCADE'))
        conn.commit()
    dimCircuit.to_sql("dimCircuit", engine, if_exists="append", index=False)
    return dimCircuit

def load_dim_constructorstandings(engine):
    dimConstructorStandings=pd.read_sql("select distinct \"constructorStandingsId\", \"constructorstandings_points\", \"constructorstandings_position\", \"constructorstandings_wins\", \"constructorstandings_positionText\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimConstructorStandings" CASCADE'))
        conn.commit()
    dimConstructorStandings.to_sql("dimConstructorStandings", engine, if_exists="append", index=False)
    return dimConstructorStandings

def load_dim_driverstandings(engine):
    dimDriverStandings=pd.read_sql("select distinct \"driverStandingsId\", \"driverstandings_points\", \"driverstandings_position\", \"driverstandings_positionText\", \"wins\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDriverStandings" CASCADE'))
        conn.commit()
    dimDriverStandings.to_sql("dimDriverStandings", engine, if_exists="append", index=False)
    return dimDriverStandings

def load_fact(engine):
    factResults=pd.read_sql("select \"id\", \"resultId\", \"raceId\", \"driverId\", \"constructorId\", \"statusId\",\"circuitId\",\"driverStandingsId\",\"constructorStandingsId\", \"dateId\", \"points\", \"position\", \"positionText\", \"positionOrder\", \"grid\", \"laps\", \"time\", \"milliseconds\", \"rank\", \"fastestLap\",\"fastestLapTime\", \"fastestLapSpeed\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "factResults" CASCADE'))
        conn.commit()
    factResults.to_sql("factResults", engine, if_exists="append", index=False)
    return factResults

def load_fact_lap(engine):
    factLap=pd.read_sql("select \"raceId\", \"driverId\", \"lap\", \"laptimes_position\", \"laptimes_milliseconds\", \"laptimes_time\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "factLap" CASCADE'))
        conn.commit()
    factLap.to_sql("factLap", engine, if_exists="append", index=False)
    return factLap

def load_fact_pitstop(engine):
    factPitstop=pd.read_sql("select \"raceId\", \"driverId\", \"stop\", \"pitstops_milliseconds\", \"pitstops_time\", \"duration\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text('TRUNCATE TABLE "factPitstop" CASCADE'))
        conn.commit()
    factPitstop.to_sql("factPitstop", engine, if_exists="append", index=False)
    return factPitstop

def load_gold(engine):
    load_dim_race(engine)
    load_dim_date(engine)
    load_dim_status(engine)
    load_dim_constructors(engine)
    load_dim_circuit(engine)
    load_dim_constructorstandings(engine)
    load_dim_driverstandings(engine)
    load_fact(engine)
    load_fact_lap(engine)
    load_fact_pitstop(engine)
    golden_layer = pd.read_sql("SELECT * FROM silver_layer", engine)
    golden_layer.to_sql("gold_layer", engine, if_exists="replace", index=False)