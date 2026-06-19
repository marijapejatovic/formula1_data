import pandas as pd
from sqlalchemy import create_engine, text
import sqlalchemy as db
import os
from dotenv import load_dotenv
from model import Base, dimCircuit, dimConstructors, dimDate

load_dotenv()

def load_dim_race(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("raceId")
            "raceId", "year", "round", "date", "race_name", "race_url",
            "quali_date", "quali_time", "races_time", "sprint_date", "sprint_time",
            "fp1_date", "fp1_time", "fp2_date", "fp2_time", "fp3_date", "fp3_time"
        FROM silver_layer
        WHERE "raceId" IS NOT NULL
        ORDER BY "raceId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimRace" CASCADE'))
    df.to_sql("dimRace", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_date(engine):
    dates = pd.date_range(start="2012-01-01", end="2023-12-31", freq="D")
    df = pd.DataFrame({
        "dateId": dates.strftime("%Y%m%d").astype(int),
        "date":   dates.date,
        "year":   dates.year,
        "month":  dates.month,
        "day":    dates.day
    })
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimDate" CASCADE'))
    df.to_sql("dimDate", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_driver(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("driverId")
            "driverId", "driverRef", "number", "code",
            "forename", "surname", "nationality", "driver_url", "dob"
        FROM silver_layer
        WHERE "driverId" IS NOT NULL
        ORDER BY "driverId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimDriver" CASCADE'))
    df.to_sql("dimDriver", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_status(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("statusId")
            "statusId", "status"
        FROM silver_layer
        WHERE "statusId" IS NOT NULL
        ORDER BY "statusId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimStatus" CASCADE'))
    df.to_sql("dimStatus", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_constructors(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("constructorId")
            "constructorId", "constructorRef", "constructor_name",
            "constructor_nationality", "constructor_url"
        FROM silver_layer
        WHERE "constructorId" IS NOT NULL
        ORDER BY "constructorId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimConstructors" CASCADE'))
    df.to_sql("dimConstructors", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_circuit(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("circuitId")
            "circuitId", "circuitRef", "circuit_name",
            "location", "country", "lat", "lng", "alt", "circuit_url"
        FROM silver_layer
        WHERE "circuitId" IS NOT NULL
        ORDER BY "circuitId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimCircuit" CASCADE'))
    df.to_sql("dimCircuit", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_constructorstandings(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("constructorStandingsId")
            "constructorStandingsId", "constructorstandings_points",
            "constructorstandings_position", "constructorstandings_wins",
            "constructorstandings_positionText"
        FROM silver_layer
        WHERE "constructorStandingsId" IS NOT NULL
        ORDER BY "constructorStandingsId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimConstructorStandings" CASCADE'))
    df.to_sql("dimConstructorStandings", engine, schema="gold", if_exists="append", index=False)
    return df

def load_dim_driverstandings(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("driverStandingsId")
            "driverStandingsId", "driverstandings_points",
            "driverstandings_position", "driverstandings_positionText", "wins"
        FROM silver_layer
        WHERE "driverStandingsId" IS NOT NULL
        ORDER BY "driverStandingsId"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."dimDriverStandings" CASCADE'))
    df.to_sql("dimDriverStandings", engine, schema="gold", if_exists="append", index=False)
    return df

def load_fact(engine):
    df = pd.read_sql("""
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
        conn.execute(text('TRUNCATE TABLE gold."factResults" CASCADE'))
    df.to_sql("factResults", engine, schema="gold", if_exists="append", index=False)
    return df

def load_fact_lap(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("raceId", "driverId", "lap")
            "raceId", "driverId", "lap",
            "laptimes_position", "laptimes_milliseconds", "laptimes_time"
        FROM silver_layer
        WHERE "lap" IS NOT NULL
        ORDER BY "raceId", "driverId", "lap"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."factLap" CASCADE'))
    df.to_sql("factLap", engine, schema="gold", if_exists="append", index=False)
    return df

def load_fact_pitstop(engine):
    df = pd.read_sql("""
        SELECT DISTINCT ON ("raceId", "driverId", "stop")
            "raceId", "driverId", "stop",
            "pitstops_milliseconds", "pitstops_time", "duration"
        FROM silver_layer
        WHERE "stop" IS NOT NULL
        ORDER BY "raceId", "driverId", "stop"
    """, engine)
    with engine.begin() as conn:
        conn.execute(text('TRUNCATE TABLE gold."factPitstop" CASCADE'))
    df.to_sql("factPitstop", engine, schema="gold", if_exists="append", index=False)
    return df

def load_gold(engine):
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS gold"))
    Base.metadata.create_all(engine)
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
    load_dim_driver(engine)
    golden_layer = pd.read_sql("SELECT * FROM silver_layer", engine)
    golden_layer.to_sql("gold_layer", engine, if_exists="replace", index=False)