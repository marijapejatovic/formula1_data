import pandas as pd

def check_row_counts(engine):
    tables=["factResults", "factLap", "factPitstop", "dimDriver", "dimRace", "dimCircuit", "dimConstructors", "dimStatus", "dimDate", "dimDriverStandings", "dimConstructorStandings"]
    for table in tables:
        count=pd.read_sql(f"select count(*) as cnt from {table}", engine)
        if count['cnt'][0]==0:
            raise ValueError(f"Table {table} is empty ingold layer")

def check_foreign_keys(engine):
    fact = pd.read_sql('SELECT "driverId", "raceId", "constructorId", "statusId", "circuitId", "driverStandingsId", "constructorStandingsId", "dateId" FROM "factResults"', engine)
    fact_lap = pd.read_sql('SELECT "driverId", "raceId" FROM "factLap"', engine)
    fact_pitstop = pd.read_sql('SELECT "driverId", "raceId" FROM "factPitstop"', engine)

    dim_driver = pd.read_sql('SELECT "driverId" FROM "dimDriver"', engine)
    dim_race = pd.read_sql('SELECT "raceId" FROM "dimRace"', engine)
    dim_constructors = pd.read_sql('SELECT "constructorId" FROM "dimConstructors"', engine)
    dim_status = pd.read_sql('SELECT "statusId" FROM "dimStatus"', engine)
    dim_circuit = pd.read_sql('SELECT "circuitId" FROM "dimCircuit"', engine)
    dim_driverstandings = pd.read_sql('SELECT "driverStandingsId" FROM "dimDriverStandings"', engine)
    dim_constructorstandings = pd.read_sql('SELECT "constructorStandingsId" FROM "dimConstructorStandings"', engine)
    dim_date = pd.read_sql('SELECT "dateId" FROM "dimDate"', engine)

    checks_fact = [
        ("driverId", dim_driver),
        ("raceId", dim_race),
        ("constructorId", dim_constructors),
        ("statusId", dim_status),
        ("circuitId", dim_circuit),
        ("driverStandingsId", dim_driverstandings),
        ("constructorStandingsId", dim_constructorstandings),
        ("dateId", dim_date),
    ]

    checks_fact_lap = [
        ("driverId", dim_driver),
        ("raceId", dim_race),
    ]

    checks_fact_pitstop = [
        ("driverId", dim_driver),
        ("raceId", dim_race),
    ]

    for col, dim in checks_fact:
        fact_ids = fact[col]
        valid_ids = dim[col]
        orphans = fact[~fact_ids.isin(valid_ids)]
        if len(orphans) > 0:
            raise ValueError(f"Orphan {col} in factResults: {len(orphans)}")

    for col, dim in checks_fact_lap:
        fact_ids = fact_lap[col]
        valid_ids = dim[col]
        orphans = fact_lap[~fact_ids.isin(valid_ids)]
        if len(orphans) > 0:
            raise ValueError(f"Orphan {col} in factLap: {len(orphans)}")

    for col, dim in checks_fact_pitstop:
        fact_ids = fact_pitstop[col]
        valid_ids = dim[col]
        orphans = fact_pitstop[~fact_ids.isin(valid_ids)]
        if len(orphans) > 0:
            raise ValueError(f"Orphan {col} in factPitstop: {len(orphans)}")

    print("All foreign key checks passed.")

def check_aggregations(engine):
    # broj vozača u dim mora odgovarati distinct driverId u fact
    dim_count = pd.read_sql('SELECT COUNT(*) as cnt FROM dim_driver', engine)
    fact_count = pd.read_sql('SELECT COUNT(DISTINCT "driverId") as cnt FROM fact', engine)
    if dim_count['cnt'][0] != fact_count['cnt'][0]:
        raise ValueError("Driver count mismatch between dim_driver and fact")
    print("Aggregation checks passed.")


def run_checks(engine):
    check_row_counts(engine)
    check_foreign_keys(engine)
    check_fact_nulls(engine)
    check_points_total(engine)
    check_aggregations(engine)
    check_kpi_thresholds(engine)