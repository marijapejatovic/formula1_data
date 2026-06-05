import sqlalchemy as db
import pandas as pd


def run_checks(engine):
    checks = {
        "drivers": """
            SELECT "driverId", COUNT(DISTINCT "driverRef") as cnt
            FROM public.silver_layer
            GROUP BY "driverId"
            HAVING COUNT(DISTINCT "driverRef") > 1
        """,
        "constructors": """
            SELECT "constructorId", COUNT(DISTINCT "constructorRef") as cnt
            FROM public.silver_layer
            GROUP BY "constructorId"
            HAVING COUNT(DISTINCT "constructorRef") > 1
        """,
        "circuits": """
            SELECT "circuitId", COUNT(DISTINCT "circuitRef") as cnt
            FROM public.silver_layer
            GROUP BY "circuitId"
            HAVING COUNT(DISTINCT "circuitRef") > 1
        """,
        "races": """
            SELECT "raceId", COUNT(DISTINCT "race_name") as cnt
            FROM public.silver_layer
            GROUP BY "raceId"
            HAVING COUNT(DISTINCT "race_name") > 1
        """,
        "results": """
            SELECT "resultId", COUNT(*) as cnt
            FROM public.silver_layer
            GROUP BY "resultId"
            HAVING COUNT(*) > 1
        """,
        "id (primary key)": """
            SELECT id, COUNT(*) as cnt
            FROM public.silver_layer
            GROUP BY id
            HAVING COUNT(*) > 1
        """,
    }

    print("=== SILVER LAYER DUPLICATE CHECKS ===\n")
    found_issues = False

    with engine.connect() as conn:
        for name, query in checks.items():
            df = pd.read_sql(db.text(query), conn)
            if df.empty:
                print(f"[OK]  {name}: no duplicates")
            else:
                found_issues = True
                print(f"[!!] {name}: {len(df)} duplicate group(s) found")
                print(df.to_string(index=False))
                print()

    if not found_issues:
        print("\nAll checks passed.")
    else:
        print("\nDuplicates detected — check the join logic in load_silver().")