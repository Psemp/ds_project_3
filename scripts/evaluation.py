import pandas as pd

from unidecode import unidecode


def get_green_rating(series: pd.Series, label_dict: dict):
    label_rating_bio = 0
    label_rating_eco = 0
    palm_rating = 0

    if pd.notna(series["labels_fr"]):
        try:
            labels = unidecode(series["labels_fr"].lower().replace(" ", "")).split(',')
            for label in labels:
                checker = [i for i in label_dict["bio"] if label in i]
                if len(checker) != 0:
                    label_rating_bio += 1
                checker = [i for i in label_dict["eco"] if label in i]
                if len(checker) != 0:
                    label_rating_eco += 1
                checker = []
        except ValueError:
            pass

    if pd.notna(series["ingredients_from_palm_oil_n"]):
        if series["ingredients_from_palm_oil_n"] != 0:
            palm_rating -= 1
    if pd.notna(series["ingredients_that_may_be_from_palm_oil_n"]):
        if series["ingredients_that_may_be_from_palm_oil_n"] != 0 and palm_rating == 0:
            palm_rating -= 1

    green_rating = label_rating_eco + label_rating_bio + palm_rating
    return green_rating
