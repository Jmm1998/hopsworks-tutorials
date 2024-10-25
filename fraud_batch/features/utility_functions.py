import numpy as np
import pandas as pd

def convert_datetime_to_microseconds(df: pd.DataFrame, datetime_column: str) -> pd.DataFrame:
    """
    Convert datetime column in a DataFrame to microseconds since the epoch.

    Parameters:
    - df (pd.DataFrame): DataFrame containing a datetime column to convert.
    - datetime_column (str): The name of the datetime column.

    Returns:
    - pd.DataFrame: DataFrame with the datetime column converted to microseconds.
    """
    df[datetime_column] = df[datetime_column].values.astype(np.int64) // 10 ** 6
    return df
