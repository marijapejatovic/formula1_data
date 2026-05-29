from sqlalchemy import Column, Integer, String, Float, Date 
from sqlalchemy.orm import declarative_base
import sqlalchemy as db

Base = declarative_base()

class DIM_Status(Base):
    __tablename__ = "dim_status"

    statusId = Column(Integer, primary_key=True)
    status = Column(String)

class DIM_Constructors(Base):
    __tablename__ = "dim_constructors"

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String)
    name_constructor = Column(String)
    nationality_constructors = Column(String)
    url_constructors=Column(String)

class DIM_Driver(Base):
    __tablename__="dim_driver"

    driverId=Column(Integer, primary_key=True)
    driverRef=Column(String)
    number=Column(Integer)
    code=Column(String)
    forename=Column(String)
    surname=Column(String)
    nationality=Column(String)
    url=Column(String)

class DIM_Race(Base):
    __tablename__="dim_race"

    raceId=Column(Integer, primary_key=True)
    year=Column(Integer)
    round=Column(Integer)
    name_race=Column(String)
    url_x=Column(String)
    quali_date=Column(db.Date)
    quali_time=Column(String)
    date=Column(db.Date)
    time_races=Column(String)
    sprint_date=Column(db.Date)
    sprint_time=Column(String)
    fp1_date = Column(Date)
    fp1_time = Column(String(200))
    fp2_date = Column(Date)
    fp2_time = Column(String(200))
    fp3_date = Column(Date)
    fp3_time = Column(String(200))

class DIM_Circuit(Base):
    __tablename__="dim_circuit"

    circuitId=Column(Integer, primary_key=True)
    circuitRef=Column(String)
    name_circuit=Column(String)
    location=Column(String)
    country=Column(String)
    lat=Column(Float)
    lng=Column(Float)
    alt=Column(Float)
    url_y=Column(String)

class DIM_DriverStandings(Base):
    __tablename__="dim_driverstandings"

    driverStandingsId=Column(Integer, primary_key=True)
    positionText_driverstandings=Column(String)
    position_driverstandings=Column(Integer)
    points_driverstandings=Column(Float)
    wins=Column(Integer)

class DIM_ConstructorStandings(Base):
    __tablename__="dim_constructorstandings"

    constructorStandingsId=Column(Integer, primary_key=True)
    positionText_constructorstandings=Column(String)
    position_constructorstandings=Column(Integer)
    points_constructorstandings=Column(Float)
    wins_constructorstandings=Column(Integer)

class DIM_date(Base):
    __tablename__="dim_date"
    dateId=Column(Integer, primary_key=True)
    date=Column(db.Date)
    year=Column(Integer)
    month=Column(Integer)
    day=Column(Integer)

class FACT(Base):
    __tablename__="fact"

    id=Column(Integer, primary_key=True)
    resultId=Column(Integer)
    raceId=Column(Integer)   
    driverId=Column(Integer)
    constructorId=Column(Integer)  
    statusId=Column(Integer)
    circuitId=Column(Integer)
    driverStandingsId=Column(Integer)
    constructorStandingsId=Column(Integer)
    grid=Column(Integer)
    position=Column(Integer)
    positionOrder=Column(Integer)
    points=Column(Float)
    laps=Column(Integer)
    milliseconds=Column(Integer)
    fastestLap=Column(Integer)
    rank=Column(Integer)
    fastestLapSpeed=Column(Float)
    stop=Column(Integer)
    positionText=Column(String)
    time=Column(String)
    fastestLapTime=Column(String)

class FACT_LAP(Base):
    __tablename__="fact_lap"

    raceId=Column(Integer, primary_key=True)   
    driverId=Column(Integer, primary_key=True)
    lap=Column(Integer, primary_key=True)
    position_laptimes=Column(Integer)
    milliseconds_laptimes=Column(Integer)
    time_laptimes=Column(String)

class FACT_PITSTOP(Base):
    __tablename__="fact_pitstop"

    raceId=Column(Integer, primary_key=True)   
    driverId=Column(Integer, primary_key=True)
    stop=Column(Integer, primary_key=True)
    duration=Column(String)
    milliseconds_pitstops=Column(Integer)
    time_pitstops=Column(String)

