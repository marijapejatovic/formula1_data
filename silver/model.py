import pandas as pd
import validators
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class SilverRow(Base):
    __tablename__ = "silver_row"

    resultId = Column(Integer, primary_key=True)
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
    number_drivers = Column(Integer)
    lap = Column(Integer)
    position_laptimes = Column(Integer)
    milliseconds_laptimes = Column(Integer)
    lap_pitstops = Column(Integer)
    milliseconds_pitstops = Column(Integer)
    stop = Column(Integer)
    driverStandingsId = Column(Integer)
    points_driverstandings = Column(Float)
    position_driverstandings = Column(Integer)
    wins = Column(Integer)
    constructorStandingsId = Column(Integer)
    points_constructorstandings = Column(Float)
    position_constructorstandings = Column(Integer)
    wins_constructorstandings = Column(Integer)
    positionText = Column(String(200))
    name_x = Column(String(200))
    name_y = Column(String(200))
    location = Column(String(200))
    country = Column(String(200))
    forename = Column(String(200))
    surname = Column(String(200))
    nationality = Column(String(200))
    nationality_constructors = Column(String(200))
    positionText_constructorstandings = Column(String(200))
    positionText_driverstandings = Column(String(200))
    status = Column(String(200))
    duration = Column(String(200))
    date = Column(Date)
    quali_date = Column(Date)
    dob = Column(Date)
    sprint_date = Column(Date)
    time = Column(String(200))
    fastestLapTime = Column(String(200))
    time_races = Column(String(200))
    quali_time = Column(String(200))
    sprint_time = Column(String(200))
    time_laptimes = Column(String(200))
    time_pitstops = Column(String(200))
    url_x = Column(String(200))
    url_y = Column(String(200))
    url = Column(String(200))
    url_constructors = Column(String(200))
    circuitRef = Column(String(200))
    driverRef = Column(String(200))
    constructorRef = Column(String(200))
    code = Column(String(200))
    circuitId = Column(Integer)


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

    def fix_time(self, columns: list) -> "DataCleaner":
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], format="%I:%M:%S %p", errors="coerce").dt.strftime("%H:%M:%S")
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