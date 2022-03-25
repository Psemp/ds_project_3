import pandas as pd


def get_green_rating(series: pd.Series, label_dict: dict):
    label_rating = 0
    palm_rating = 0

    labels = series["labels_fr"].lower().replace(" ", "").split(',')

    for label in labels:
        checker = [i for i in label_dict["negative"] if label in i]
        if len(checker) != 0:
            label_rating -= 1
        checker = [i for i in label_dict["positive"] if label in i]
        if len(checker) != 0:
            label_rating += 1
        checker = []

    if series["ingredients_from_palm_oil_n"].notna():
        if series["ingredients_from_palm_oil_n"] != 0:
            palm_rating -= 1
    if series["ingredients_that_may_be_from_palm_oil_n"].notna():
        if series["ingredients_that_may_be_from_palm_oil_n"] != 0 and palm_rating == 0:
            palm_rating -= 1

    green_rating = label_rating + palm_rating
    return green_rating
