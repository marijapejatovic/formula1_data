import pandas as pd

def check_nulls(df):
    nulls = df.isnull().sum()
    print("Null values in each column:")
    print(nulls)
def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
def check_data_types(df):
    print("Data types of each column:")
    print(df.dtypes)    
def check_row_counts(df, df_bronze):
    print(f"Number of rows in silver layer: {len(df)}")
    print(f"Number of rows in bronze layer: {len(df_bronze)}")
    if len(df)!=len(df_bronze):
        raise ValueError("Row count mismatch between silver and bronze layers")
def check_negative_values(df):
    columns = ["points", "duration", "pitstops_milliseconds", "lap_pitstops", "year", "round", "driverstandings_points", "driverstandings_position", "constructorstandings_points", "constructorstandings_position", "positionOrder", "grid", "laps", "rank", "fastestLap", "fastestLapSpeed"]
    for col in columns:
        if (df[col]<0).any():
            raise ValueError(f"Negative values found in column {col} in silver layer")
def check_year(df):
    if (df["year"].dropna() < 2012).any() or (df["year"].dropna() > 2023).any():
        raise ValueError("Year out of range in silver layer")
def check_dates(df):
    columns = ["quali_date", "sprint_date", "dob"]
    for col in columns:
        mask = df[col].notna() & df["date"].notna()
        if (df.loc[mask, col] >df.loc[mask, "date"]).any():
            raise ValueError(f"{col} is not before race date in silver layer")

def run_checks(engine):
    df = pd.read_sql("SELECT * FROM silver_layer", engine)
    df_bronze = pd.read_sql("SELECT * FROM bronze_layer", engine)
    check_nulls(df)
    check_duplicates(df)
    check_data_types(df)
    check_row_counts(df, df_bronze)
    check_negative_values(df)
    check_year(df)
    check_dates(df)
    
