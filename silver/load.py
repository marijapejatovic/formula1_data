from model import metadata_obj, DataCleaner
import pandas as pd

def load_silver(engine):
    metadata_obj.create_all(engine)
    
    bronze_df = pd.read_sql("SELECT * FROM bronze_row", engine)
    
    silver = DataCleaner(bronze_df, "silver_row")
    silver_row = (silver
        .standardize_text_columns(["positionText", "name_x", "name_y", "location", "country", "forename", "surname", "nationality", "nationality_constructors", "positionText_constructorstandings", "positionText_driverstandings", "status", "duration"])
        .fix_dates_columns(["date", "quali_date", "dob", "sprint_date"])
        .fix_time(["time", "fastestLapTime", "time_races", "quali_time", "sprint_time", "time_laptimes", "time_pitstops"])
        .fix_numerical(["resultId", "raceId", "driverId", "constructorId", "number", "grid", "position", "positionOrder", "points", "laps", "milliseconds", "fastestLap", "rank", "fastestLapSpeed", "statusId", "year", "round", "lat", "lng", "alt", "number_drivers", "lap", "position_laptimes", "milliseconds_laptimes", "lap_pitstops", "milliseconds_pitstops", "stop", "driverStandingsId", "points_driverstandings", "position_driverstandings", "wins", "constructorStandingsId", "points_constructorstandings", "position_constructorstandings", "wins_constructorstandings", "circuitId"])
        .standardize_url(["url_x", "url_y", "url", "url_constructors"])
        .standardize_lowercase(["circuitRef", "driverRef", "constructorRef"])
        .standardize_uppercase(["code"])
    )
    
    silver_row.df.to_sql("silver_row", engine, if_exists="replace", index=False)
    return silver_row.df