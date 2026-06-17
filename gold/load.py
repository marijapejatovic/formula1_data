import pandas as pd
from sqlalchemy import create_engine, text
import sqlalchemy as db
import os
from dotenv import load_dotenv
from model import Base

load_dotenv()
<<<<<<< HEAD
def load_dim_race(engine):
    Base.metadata.create_all(engine)
    dim_race=pd.read_sql("select distinct \"raceId\", \"year\", \"round\", \"date\", \"name_race\", \"url_x\", \"quali_date\", \"quali_time\", \"time_races\", \"sprint_date\", \"sprint_time\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_race CASCADE"))
        conn.commit()
    dim_race.to_sql("dim_race", engine, if_exists="append", index=False)
    return dim_race

def load_dim_driver(engine):
    Base.metadata.create_all(engine)
    dim_driver=pd.read_sql("select distinct \"driverId\", \"driverRef\", \"number\", \"code\", \"forename\", \"surname\", \"nationality\", \"url\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_driver CASCADE"))
        conn.commit()
    dim_driver.to_sql("dim_driver", engine, if_exists="append", index=False)
    return dim_driver   
def load_dim_date(engine):
    Base.metadata.create_all(engine)
    
    dates = pd.date_range(start="2012-01-01", end="2023-12-31", freq="D")
    
    dim_date = pd.DataFrame({
=======

def load_dim_race(engine):
    dimRace = pd.read_sql("""
        SELECT DISTINCT ON ("raceId")
            "raceId", "year", "round", "date", "race_name", "race_url",
            "quali_date", "quali_time", "races_time", "sprint_date", "sprint_time",
            "fp1_date", "fp1_time", "fp2_date", "fp2_time", "fp3_date", "fp3_time"
        FROM silver_layer
        WHERE "raceId" IS NOT NULL
        ORDER BY "raceId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimRace" CASCADE'))
    dimRace.to_sql("dimRace", engine, if_exists="append", index=False)
    return dimRace
def load_dim_date(engine):
    dates = pd.date_range(start="2012-01-01", end="2023-12-31", freq="D")
    dimDate = pd.DataFrame({
>>>>>>> dev_new
        "dateId": dates.strftime("%Y%m%d").astype(int),
        "date":   dates.date,
        "year":   dates.year,
        "month":  dates.month,
        "day":    dates.day
    })
<<<<<<< HEAD
    
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_date CASCADE"))
        conn.commit()
    
    dim_date.to_sql("dim_date", engine, if_exists="append", index=False)
    return dim_date

def load_dim_status(engine):
    Base.metadata.create_all(engine)
    dim_status=pd.read_sql("select distinct \"statusId\", \"status\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_status CASCADE"))
        conn.commit()
    dim_status.to_sql("dim_status", engine, if_exists="append", index=False)
    return dim_status

def load_dim_constructors(engine):  
    Base.metadata.create_all(engine)
    dim_constructors=pd.read_sql("select distinct \"constructorId\", \"constructorRef\", \"name_constructor\", \"nationality_constructors\", \"url_constructors\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_constructors CASCADE"))
        conn.commit()   
    dim_constructors.to_sql("dim_constructors", engine, if_exists="append", index=False)
    return dim_constructors

def load_dim_circuit(engine):
    Base.metadata.create_all(engine)
    dim_circuit=pd.read_sql("select distinct \"circuitId\", \"circuitRef\", \"name_circuit\", \"location\", \"country\", \"lat\", \"lng\", \"alt\", \"url_y\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_circuit CASCADE"))
        conn.commit()   
    dim_circuit.to_sql("dim_circuit", engine, if_exists="append", index=False)
    return dim_circuit

def load_dim_constructorstandings(engine):
    Base.metadata.create_all(engine)
    dim_constructorstandings=pd.read_sql("select distinct \"constructorStandingsId\", \"points_constructorstandings\", \"position_constructorstandings\", \"wins_constructorstandings\", \"positionText_constructorstandings\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_constructorstandings CASCADE"))
        conn.commit()   
    dim_constructorstandings.to_sql("dim_constructorstandings", engine, if_exists="append", index=False)
    return dim_constructorstandings

def load_fact(engine):
    Base.metadata.create_all(engine)
    fact=pd.read_sql("select \"id\", \"resultId\", \"raceId\", \"driverId\", \"constructorId\", \"statusId\",\"circuitId\",\"driverStandingsId\",\"constructorStandingsId\", \"dateId\", \"points\", \"position\", \"positionText\", \"positionOrder\", \"grid\", \"laps\", \"time\", \"milliseconds\", \"rank\", \"fastestLap\",\"fastestLapTime\", \"fastestLapSpeed\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE fact CASCADE"))
        conn.commit()   
    fact.to_sql("fact", engine, if_exists="append", index=False)
    return fact

def load_fact_lap(engine):
    Base.metadata.create_all(engine)
    fact_lap=pd.read_sql("select  \"raceId\", \"driverId\", \"lap\", \"position_laptimes\", \"milliseconds_laptimes\", \"time_laptimes\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE fact_lap CASCADE"))
        conn.commit()   
    fact_lap.to_sql("fact_lap", engine, if_exists="append", index=False)
    return fact_lap

def load_fact_lappitstops(engine):
    Base.metadata.create_all(engine)
    fact_lappitstops=pd.read_sql("select  \"raceId\", \"driverId\", \"stop\", \"milliseconds_pitstops\", \"time_pitstops\", \"duration\" from silver_layer", engine)
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE fact_lappitstops CASCADE"))
        conn.commit()   
    fact_lappitstops.to_sql("fact_lappitstops", engine, if_exists="append", index=False)
    return fact_lappitstops

def load_gold(engine):
    Base.metadata.create_all(engine)
    load_dim_race(engine)
    load_dim_driver(engine)
=======
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDate" CASCADE'))
    dimDate.to_sql("dimDate", engine, if_exists="append", index=False)
    return dimDate
def load_dim_driver(engine):
    dim_driver = pd.read_sql("""
        SELECT DISTINCT ON ("driverId")
            "driverId", "driverRef", "number", "code",
            "forename", "surname", "nationality", "driver_url", "dob"
        FROM silver_layer
        WHERE "driverId" IS NOT NULL
        ORDER BY "driverId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDriver" CASCADE'))
    dim_driver.to_sql("dimDriver", engine, if_exists="append", index=False)
    return dim_driver

def load_dim_status(engine):
    dimStatus = pd.read_sql("""
        SELECT DISTINCT ON ("statusId")
            "statusId", "status"
        FROM silver_layer
        WHERE "statusId" IS NOT NULL
        ORDER BY "statusId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimStatus" CASCADE'))
    dimStatus.to_sql("dimStatus", engine, if_exists="append", index=False)
    return dimStatus

def load_dim_constructors(engine):
    dimConstructors = pd.read_sql("""
        SELECT DISTINCT ON ("constructorId")
            "constructorId", "constructorRef", "constructor_name",
            "constructor_nationality", "constructor_url"
        FROM silver_layer
        WHERE "constructorId" IS NOT NULL
        ORDER BY "constructorId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimConstructors" CASCADE'))
    dimConstructors.to_sql("dimConstructors", engine, if_exists="append", index=False)
    return dimConstructors

def load_dim_circuit(engine):
    dimCircuit = pd.read_sql("""
        SELECT DISTINCT ON ("circuitId")
            "circuitId", "circuitRef", "circuit_name",
            "location", "country", "lat", "lng", "alt", "circuit_url"
        FROM silver_layer
        WHERE "circuitId" IS NOT NULL
        ORDER BY "circuitId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimCircuit" CASCADE'))
    dimCircuit.to_sql("dimCircuit", engine, if_exists="append", index=False)
    return dimCircuit

def load_dim_constructorstandings(engine):
    dimConstructorStandings = pd.read_sql("""
        SELECT DISTINCT ON ("constructorStandingsId")
            "constructorStandingsId", "constructorstandings_points",
            "constructorstandings_position", "constructorstandings_wins",
            "constructorstandings_positionText"
        FROM silver_layer
        WHERE "constructorStandingsId" IS NOT NULL
        ORDER BY "constructorStandingsId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimConstructorStandings" CASCADE'))
    dimConstructorStandings.to_sql("dimConstructorStandings", engine, if_exists="append", index=False)
    return dimConstructorStandings

def load_dim_driverstandings(engine):
    dimDriverStandings = pd.read_sql("""
        SELECT DISTINCT ON ("driverStandingsId")
            "driverStandingsId", "driverstandings_points",
            "driverstandings_position", "driverstandings_positionText", "wins"
        FROM silver_layer
        WHERE "driverStandingsId" IS NOT NULL
        ORDER BY "driverStandingsId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "dimDriverStandings" CASCADE'))
    dimDriverStandings.to_sql("dimDriverStandings", engine, if_exists="append", index=False)
    return dimDriverStandings

def load_fact(engine):
    factResults = pd.read_sql("""
        SELECT DISTINCT ON ("resultId")
            "id", "resultId", "raceId", "driverId", "constructorId", "statusId",
            "circuitId", "driverStandingsId", "constructorStandingsId", "dateId",
            "points", "position", "positionText", "positionOrder", "grid", "laps",
            "time", "milliseconds", "rank", "fastestLap", "fastestLapTime", "fastestLapSpeed"
        FROM silver_layer
        WHERE "resultId" IS NOT NULL
        ORDER BY "resultId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "factResults" CASCADE'))
    factResults.to_sql("factResults", engine, if_exists="append", index=False)
    return factResults

def load_fact_lap(engine):
    factLap = pd.read_sql("""
        SELECT DISTINCT ON ("raceId", "driverId", "lap")
            "raceId", "driverId", "lap",
            "laptimes_position", "laptimes_milliseconds", "laptimes_time"
        FROM silver_layer
        WHERE "lap" IS NOT NULL
        ORDER BY "raceId", "driverId", "lap"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "factLap" CASCADE'))
    factLap.to_sql("factLap", engine, if_exists="append", index=False)
    return factLap

def load_fact_pitstop(engine):
    factPitstop = pd.read_sql("""
        SELECT DISTINCT ON ("raceId", "driverId", "stop")
            "raceId", "driverId", "stop",
            "pitstops_milliseconds", "pitstops_time", "duration"
        FROM silver_layer
        WHERE "stop" IS NOT NULL
        ORDER BY "raceId", "driverId", "stop"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE "factPitstop" CASCADE'))
    factPitstop.to_sql("factPitstop", engine, if_exists="append", index=False)
    return factPitstop

def load_gold(engine):
    load_dim_race(engine)
>>>>>>> dev_new
    load_dim_date(engine)
    load_dim_status(engine)
    load_dim_constructors(engine)
    load_dim_circuit(engine)
    load_dim_constructorstandings(engine)
<<<<<<< HEAD
    load_fact(engine)
    load_fact_lap(engine)
    load_fact_lappitstops(engine)

    golden_layer = pd.read_sql("SELECT * FROM silver_layer", engine)
    with engine.connect() as conn:
        if db.inspect(engine).has_table("golden_layer"):
            conn.execute(text("TRUNCATE TABLE golden_layer CASCADE"))
            conn.commit()
    golden_layer.to_sql("golden_layer", engine, if_exists="append", index=False)
    return golden_layer
=======
    load_dim_driverstandings(engine)
    load_fact(engine)
    load_fact_lap(engine)
    load_fact_pitstop(engine)
    load_dim_driver(engine)
    golden_layer = pd.read_sql("SELECT * FROM silver_layer", engine)
    golden_layer.to_sql("gold_layer", engine, if_exists="replace", index=False)
>>>>>>> dev_new
