import pandas as pd
import validators
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import declarative_base
import sqlalchemy as db


Base = declarative_base()


class SilverRow(Base):
    __tablename__ = "silver_layer"
    __table_args__ = {"schema": "silver"}
    id=db.Column(db.String(200), primary_key=True)

    resultId = Column(Integer)
    raceId = Column(Integer)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer)
    fastestLapSpeed = Column(Float)
    statusId = Column(Integer)
    year = Column(Integer)
    round = Column(Integer)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Float)
    drivers_number = Column(Integer)
    lap = Column(Integer)
    laptimes_position = Column(Integer)
    laptimes_milliseconds = Column(Integer)
    lap_pitstops = Column(Integer)
    pitstops_milliseconds = Column(Integer)
    stop = Column(Integer)
    driverStandingsId = Column(Integer)
    driverstandings_points = Column(Float)
    driverstandings_position = Column(Integer)
    wins = Column(Integer)
    constructorStandingsId = Column(Integer)
    constructorstandings_points = Column(Float)
    constructorstandings_position = Column(Integer)
    constructorstandings_wins = Column(Integer)
    positionText = Column(String(200))
    race_name = Column(String(200))
    circuit_name = Column(String(200))
    location = Column(String(200))
    country = Column(String(200))
    forename = Column(String(200))
    surname = Column(String(200))
    nationality = Column(String(200))
    constructor_nationality = Column(String(200))
    constructorstandings_positionText = Column(String(200))
    driverstandings_positionText = Column(String(200))
    status = Column(String(200))
    duration = Column(Float)
    date = Column(Date)
    quali_date = Column(Date)
    dob = Column(Date)
    sprint_date = Column(Date)
    time = Column(String(200))
    fastestLapTime = Column(String(200))
    races_time = Column(String(200))
    quali_time = Column(String(200))
    sprint_time = Column(String(200))
    laptimes_time = Column(String(200))
    pitstops_time = Column(String(200))
    race_url = Column(String(200))
    circuit_url = Column(String(200))
    driver_url = Column(String(200))
    constructor_url = Column(String(200))
    circuitRef = Column(String(200))
    driverRef = Column(String(200))
    constructorRef = Column(String(200))
    code = Column(String(200))
    circuitId = Column(Integer)
    fp1_date = Column(Date)
    fp1_time = Column(String(200))
    fp2_date = Column(Date)
    fp2_time = Column(String(200))
    fp3_date = Column(Date)
    fp3_time = Column(String(200))
    constructor_name = Column(String(200))
    dateId = Column(Integer)




class DataCleaner:
    def __init__(self, df: pd.DataFrame, name: str):
        self.df = df.copy()
        self.name = name

    def standardize_text_columns(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = self.df[col].astype(str)
            self.df[col] = self.df[col].str.strip().str.title()
        return self

    def fix_dates_columns(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], format="mixed", errors="coerce")
        return self


    def fix_numerical(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = pd.to_numeric(self.df[col], errors="coerce")
        return self

    def standardize_lowercase(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = self.df[col].str.strip().str.lower()
        return self

    def standardize_uppercase(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = self.df[col].str.strip().str.upper()
        return self

    def standardize_url(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = self.df[col].astype(str).str.strip().apply(
                lambda x: x if validators.url(x) else pd.NA
            )
        return self