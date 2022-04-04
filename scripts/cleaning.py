import pandas as pd
import numpy as np


def is_aberration(series: pd.Series, hundred_g_list: list) -> bool:
    """if a non na col of a 100g is > 100 or < 0, returns True"""

    for col in hundred_g_list:
        if pd.notna(series[col]):
            if float(series[col]) > 100 or float(series[col]) < 0:
                return True

    return False


def remove_outliers(column_eval: str, col_subset: str, value_list: list, df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the IQR (Inter Quartile Range) for each column value of the column_subset of a DataFrame using
     the column to evaluate.
    Applies the method to clean the data for each value in the subset and returns a cleaned dataframe

    Args:
     - column_eval : name of the column to evaluate, dtype must be int or float
     - col_subset : column containing multiple values. The dataframe can be split using this and :
     - value_list : the list of values expected in the subset
     - df : the dataframe to clean

    Returns : pd.DataFrame
    """
    dtype = str(df[column_eval].dtype)
    if not (dtype.startswith("int") or dtype.startswith("float")):
        print(not dtype.startswith("int") or not dtype.startswith("float"))
        print(dtype)
        raise Exception("Error : Data Type not a number")

    cleaned_df = pd.DataFrame(columns=df.columns)
    for column_value in value_list:
        evaluated = df[df[col_subset] == column_value]
        q3, q1 = np.percentile(evaluated[column_eval], [75, 25])
        iqr = (q3 - q1) * 1.5
        q3_max = q3 + iqr
        q1_min = q1 - iqr
        cleaned_df = pd.concat(
                                [
                                    cleaned_df,
                                    evaluated[(evaluated[column_eval] < q3_max) & (evaluated[column_eval] > q1_min)]
                                ]
                                )

    return cleaned_df
