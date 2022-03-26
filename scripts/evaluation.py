import pandas as pd
import numpy as np

from unidecode import unidecode


def get_green_rating(series: pd.Series, bio_list: list):
    """
    Takes a series and defines if a label is in bio_list to find if product is organic
    and evaluates possible amount of palm oil, returns dict of results
    """
    result_dict = {
        "org": np.nan,
        "palm_oil": np.nan
    }

    if pd.notna(series["labels_fr"]):
        organic = False
        try:
            labels = unidecode(series["labels_fr"].lower().replace(" ", "")).split(',')
            for label in labels:
                checker = [i for i in bio_list if label in i]
                if len(checker) != 0 and not organic:
                    result_dict["org"] = True
        except (ValueError, AttributeError):
            pass

    if pd.notna(series["ingredients_from_palm_oil_n"]):
        contains_palm = False

        if int(series["ingredients_from_palm_oil_n"]) > 0:
            contains_palm = True
            result_dict["palm_oil"] = True
            return result_dict
        elif int(series["ingredients_from_palm_oil_n"]) == 0:
            pass

    if pd.notna(series["ingredients_that_may_be_from_palm_oil_n"]) and not contains_palm:
        if int(series["ingredients_that_may_be_from_palm_oil_n"]) > 0:
            result_dict["palm_oil"] = True
        elif int(series["ingredients_that_may_be_from_palm_oil_n"]) == 0:
            series["palm_oil"] = False

    return result_dict
