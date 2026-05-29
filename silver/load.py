from model import Base, DataCleaner
import pandas as pd
import sqlalchemy as db

def load_silver(engine):
    Base.metadata.create_all(engine)
    
    bronze_df = pd.read_sql("SELECT * FROM bronze_layer", engine)
    
    silver = DataCleaner(bronze_df, "silver_layer")
    silver_layer = (silver
        .standardize_text_columns(["positionText", "name_race", "name_circuit", "location", "country", "forename", "surname", "nationality", "nationality_constructors", "positionText_constructorstandings", "positionText_driverstandings", "status","fp1_time", "fp2_time", "fp3_time", "quali_time", "sprint_time", "time", "fastestLapTime", "time_races", "time_laptimes", "time_pitstops","name_constructor"])
        .fix_dates_columns(["date", "quali_date", "dob", "sprint_date", "fp1_date", "fp2_date", "fp3_date"])
        .fix_numerical(["resultId", "duration","raceId", "driverId", "constructorId", "number", "grid", "position", "positionOrder", "points", "laps", "milliseconds", "fastestLap", "rank", "fastestLapSpeed", "statusId", "year", "round", "lat", "lng", "alt", "number_drivers", "lap", "position_laptimes", "milliseconds_laptimes", "lap_pitstops", "milliseconds_pitstops", "stop", "driverStandingsId", "points_driverstandings", "position_driverstandings", "wins", "constructorStandingsId", "points_constructorstandings", "position_constructorstandings", "wins_constructorstandings", "circuitId"])
        .standardize_url(["url_x", "url_y", "url", "url_constructors"])
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