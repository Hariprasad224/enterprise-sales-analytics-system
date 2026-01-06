import pandas as pd
from pathlib import Path
from .db import engine

SQL_DIR = Path("db_scripts")

def run_sql(file_name: str) -> pd.DataFrame:
    sql_path = SQL_DIR / file_name

    with open(sql_path, "r") as f:
        query = f.read()

    df = pd.read_sql(query, engine)

    # JSON-safe cleanup
    df = df.replace([float("inf"), float("-inf")], 0).fillna(0)
    return df
