from model import Base, DataCleaner
import pandas as pd
import sqlalchemy as db

def load_silver(engine):
    Base.metadata.create_all(engine)
    
    bronze_df = pd.read_sql("SELECT * FROM bronze_layer", engine)
    bronze_df = bronze_df.rename(columns={
    "name": "constructor_name",
    "name_x": "race_name", 
    "name_y": "circuit_name",
    "number_drivers": "drivers_number",
    "position_laptimes": "laptimes_position",
    "milliseconds_laptimes": "laptimes_milliseconds",
    "milliseconds_pitstops": "pitstops_milliseconds",
    "points_driverstandings": "driverstandings_points",
    "position_driverstandings": "driverstandings_position",
    "wins_constructorstandings": "constructorstandings_wins",
    "nationality_constructors": "constructor_nationality",
    "positionText_constructorstandings": "constructorstandings_positionText",
    "positionText_driverstandings": "driverstandings_positionText",
    "time_laptimes": "laptimes_time",
    "time_pitstops": "pitstops_time",
    "url_x": "race_url",
    "url_y": "circuit_url",
    "url_constructors": "constructor_url",
    "url": "driver_url",
    "time_races" : "races_time",
    "points_constructorstandings": "constructorstandings_points",
    "position_constructorstandings": "constructorstandings_position",
    



})
    silver = DataCleaner(bronze_df, "silver_layer")
    silver_layer= (silver
        .standardize_text_columns(["positionText", "race_name", "circuit_name", "location", "country", "forename", "surname", "nationality", "constructor_nationality", "constructorstandings_positionText", "driverstandings_positionText", "status","fp1_time", "fp2_time", "fp3_time", "quali_time", "sprint_time", "time", "fastestLapTime", "races_time", "laptimes_time", "pitstops_time","constructor_name"])
        .fix_dates_columns(["date", "quali_date", "dob", "sprint_date", "fp1_date", "fp2_date", "fp3_date"])
        .fix_numerical(["resultId", "duration","raceId", "driverId", "constructorId", "number", "grid", "position", "positionOrder", "points", "laps", "milliseconds", "fastestLap", "rank", "fastestLapSpeed", "statusId", "year", "round", "lat", "lng", "alt", "drivers_number", "lap", "laptimes_position", "laptimes_milliseconds", "lap_pitstops", "pitstops_milliseconds", "stop", "driverStandingsId", "driverstandings_points", "driverstandings_position", "wins", "constructorStandingsId", "constructorstandings_points", "constructorstandings_position", "constructorstandings_wins", "circuitId"])
        .standardize_url(["race_url", "circuit_url", "driver_url", "constructor_url"])
        .standardize_lowercase(["circuitRef", "driverRef", "constructorRef"])
        .standardize_uppercase(["code"])
    )
    with engine.connect() as conn:
        if db.inspect(engine).has_table("silver_layer"):
            conn.execute(db.text("TRUNCATE TABLE silver_layer CASCADE"))
            conn.commit()
    silver_layer.df=silver_layer.df.rename(columns={"Unnamed: 0": "id"})
    silver_layer.df["dateId"] = pd.to_datetime(silver_layer.df["date"]).dt.strftime("%Y%m%d").astype("Int64")
    silver_layer.df.to_sql("silver_layer", engine, if_exists="append", index=False)
    return silver_layer.df