import pandas as pd

from .config import RAW_DATA_DIR


def load_raw() -> pd.DataFrame:
    """The immutable raw extract. Swap sample.csv for a real export to validate."""
    return pd.read_csv(RAW_DATA_DIR / "sample.csv", parse_dates=["period"])
