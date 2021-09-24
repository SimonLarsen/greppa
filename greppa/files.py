import pandas as pd


ENDINGS = {"parquet": [".parquet"]}

READERS = {"parquet": pd.read_parquet}

WRITERS = {"parquet": pd.DataFrame.to_parquet}


def guess_file_type(path: str) -> str:
    lpath = str(path).lower()

    if "." not in lpath:
        raise RuntimeError("Input file does not have a file ending.")

    if lpath.endswith(".parquet"):
        return "parquet"
    else:
        raise RuntimeError("Could not infer file type from filename.")


def read_file(path: str, type: str) -> pd.DataFrame:
    if type not in READERS:
        raise RuntimeError(f"Unsupported file type {type}.")

    reader = READERS[type]
    return reader(path)


def write_file(df: pd.DataFrame, path: str, type: str) -> None:
    if type not in WRITERS:
        raise RuntimeError(f"Unsupported file type {type}.")

    writer = WRITERS[type]
    writer(df, path)
