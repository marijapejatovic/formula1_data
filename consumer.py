from kafka import KafkaConsumer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
import json
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class BronzeWeather(Base):
    __tablename__ = "bronze_weather"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_key = Column(String)
    meeting_key = Column(String)
    air_temperature = Column(String)
    track_temperature = Column(String)
    humidity = Column(String)
    pressure = Column(String)
    rainfall = Column(String)
    wind_speed = Column(String)
    wind_direction = Column(String)
    date = Column(String)

engine = create_engine(os.getenv("DATABASE_URL"))
Base.metadata.create_all(engine)

consumer = KafkaConsumer(
    'f1-data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
)

for message in consumer:
    data = message.value
    print('Received:', data)

    with Session(engine) as session:
        weather = BronzeWeather(
            session_key=str(data.get('session_key')),
            meeting_key=str(data.get('meeting_key')),
            air_temperature=str(data.get('air_temperature')),
            track_temperature=str(data.get('track_temperature')),
            humidity=str(data.get('humidity')),
            pressure=str(data.get('pressure')),
            rainfall=str(data.get('rainfall')),
            wind_speed=str(data.get('wind_speed')),
            wind_direction=str(data.get('wind_direction')),
            date=str(data.get('date')),
        )
        session.add(weather)
        session.commit()
        print('Saved to DB:', data.get('session_key'))