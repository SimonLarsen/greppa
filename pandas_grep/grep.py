import pandas as pd


def grep(df: pd.DataFrame, pattern: str) -> pd.DataFrame:
    return df.query(pattern)
