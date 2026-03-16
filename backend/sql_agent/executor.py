import pandas as pd
from sqlalchemy import text
from backend.db import engine

def execute_sql(query):
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df