import pandas as pd
import validators
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import declarative_base
import sqlalchemy as db


Base = declarative_base()


class SilverRow(Base):
    __tablename__ = "silver_row"
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
    
    TIMEZONE_MAP = {
    'Melbourne': 'Australia/Melbourne',
    'Kuala Lumpur': 'Asia/Kuala_Lumpur',
    'Shanghai': 'Asia/Shanghai',
    'Sakhir': 'Asia/Bahrain',
    'Montmeló': 'Europe/Madrid',
    'Monte-Carlo': 'Europe/Monaco',
    'Montreal': 'America/Toronto',
    'Valencia': 'Europe/Madrid',
    'Silverstone': 'Europe/London',
    'Hockenheim': 'Europe/Berlin',
    'Budapest': 'Europe/Budapest',
    'Spa': 'Europe/Brussels',
    'Monza': 'Europe/Rome',
    'Marina Bay': 'Asia/Singapore',
    'Suzuka': 'Asia/Tokyo',
    'Uttar Pradesh': 'Asia/Kolkata',
    'Abu Dhabi': 'Asia/Dubai',
    'Austin': 'America/Chicago',
    'São Paulo': 'America/Sao_Paulo',
    'Nürburg': 'Europe/Berlin',
    'Yeongam County': 'Asia/Seoul',
    'Spielberg': 'Europe/Vienna',
    'Sochi': 'Europe/Moscow',
    'Mexico City': 'America/Mexico_City',
    'Baku': 'Asia/Baku',
    'Imola': 'Europe/Rome',
    'Portimão': 'Europe/Lisbon',
    'Le Castellet': 'Europe/Paris',
    'Istanbul': 'Europe/Istanbul',
    'Jeddah': 'Asia/Riyadh',
    'Miami': 'America/New_York',
    'Zandvoort': 'Europe/Amsterdam',
    'Mugello': 'Europe/Rome',
    'Al Daayen': 'Asia/Qatar',
}
    def fix_time(self, columns:list) -> "DataCleaner":
        for col in columns:
            mask_ampm=self.df[col].str.contains(r'AM|PM', na=False)

            dt=pd.to_datetime(self.df.loc[mask_ampm, col], format='mixed', errors='coerce')

            for location, timezone in self.TIMEZONE_MAP.items():
                loc_mask=(self.df["location"]==location) & mask_ampm
                if loc_mask.any():
                    self.df.loc[loc_mask, column]=(
                        dt[loc_mask]
                        .dt.tz_localize(timezone, ambiguous="NaT", nonexistent="NaT")
                        .dt.tz_convert("UTC")
                        .dt.strftime("%H:%M:%S")
                    )

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