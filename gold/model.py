<<<<<<< HEAD
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
=======
from sqlalchemy import Column, Integer, String, Float, Date 
from sqlalchemy.orm import declarative_base
import sqlalchemy as db

Base = declarative_base()

class dimStatus(Base):
    __tablename__ = "dim_status"

    statusId = Column(Integer, primary_key=True)
    status = Column(String)

class dimConstructors(Base):
    __tablename__ = "dim_constructors"

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String)
    constructor_name = Column(String)
    constructor_nationality = Column(String)
    constructor_url = Column(String)

class dimDriver(Base):
    __tablename__ = "dim_driver"

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String)
    number = Column(Integer)
    code = Column(String)
    forename = Column(String)
    surname = Column(String)
    nationality = Column(String)
    driver_url = Column(String)
    dob = Column(Date)

class dimRace(Base):
    __tablename__ = "dim_race"

    raceId = Column(Integer, primary_key=True)
    year = Column(Integer)
    round = Column(Integer)
    race_name = Column(String)
    race_url = Column(String)
    quali_date = Column(Date)
    quali_time = Column(String)
    date = Column(Date)
    races_time = Column(String)
    sprint_date = Column(Date)
    sprint_time = Column(String)
    fp1_date = Column(Date)
    fp1_time = Column(String)
    fp2_date = Column(Date)
    fp2_time = Column(String)
    fp3_date = Column(Date)
    fp3_time = Column(String)

class dimCircuit(Base):
    __tablename__ = "dimCircuit"

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String)
    circuit_name = Column(String)
    location = Column(String)
    country = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Float)
    circuit_url = Column(String)

class dimDriverStandings(Base):
    __tablename__ = "dimDriverStandings"

    driverStandingsId = Column(Integer, primary_key=True)
    driverstandings_positionText = Column(String)
    driverstandings_position = Column(Integer)
    driverstandings_points = Column(Float)
    wins = Column(Integer)

class dimConstructorStandings(Base):
    __tablename__ = "dimConstructorStandings"

    constructorStandingsId = Column(Integer, primary_key=True)
    constructorstandings_positionText = Column(String)
    constructorstandings_position = Column(Integer)
    constructorstandings_points = Column(Float)
    constructorstandings_wins = Column(Integer)

class dimDate(Base):
    __tablename__ = "dimDate"

    dateId = Column(Integer, primary_key=True)
    date = Column(Date)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)

class factResults(Base):
    __tablename__ = "factResults"

    id = Column(Integer, primary_key=True)
    resultId = Column(Integer)
    raceId = Column(Integer)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    statusId = Column(Integer)
    circuitId = Column(Integer)
    driverStandingsId = Column(Integer)
    constructorStandingsId = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer)
    fastestLapSpeed = Column(Float)
    stop = Column(Integer)
    positionText = Column(String)
    time = Column(String)
    fastestLapTime = Column(String)
    dateId = Column(Integer)

class factLap(Base):
    __tablename__ = "factLap"

    raceId = Column(Integer, primary_key=True)
    driverId = Column(Integer, primary_key=True)
    lap = Column(Integer, primary_key=True)
    laptimes_position = Column(Integer)
    laptimes_milliseconds = Column(Integer)
    laptimes_time = Column(String)

class factPitstop(Base):
    __tablename__ = "factPitstop"

    raceId = Column(Integer, primary_key=True)
    driverId = Column(Integer, primary_key=True)
    stop = Column(Integer, primary_key=True)
    duration = Column(Float)
    pitstops_milliseconds = Column(Integer)
    pitstops_time = Column(String)
>>>>>>> dev_new
