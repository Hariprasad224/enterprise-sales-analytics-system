import pandas as pd

def explain_result(df):

    if df.empty:
        return "No records found."

    first_row = df.iloc[0].to_dict()

    return f"Returned {len(df)} rows. Top result: {first_row}"