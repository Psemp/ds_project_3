import pandas as pd


def is_aberration(series: pd.Series, hundred_g_list: list) -> bool:
    """if a non na col of a 100g is > 100 or < 0, returns True"""

    for col in hundred_g_list:
        if pd.notna(series[col]):
            if float(series[col]) > 100 or float(series[col]) < 0:
                return True

    return False
