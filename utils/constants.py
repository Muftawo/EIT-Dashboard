import os
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

PRE_PROGRAM_DATA = os.path.join(BASE_DIR, "data/pre_program_responses.csv")
MID_PROGRAM_DATA = os.path.join(BASE_DIR, "data/mid_program_responses.csv")

COLOR_DICT_RATING_SCALE = {
    "Very Poor": "red",
    "Poor": "orange",
    "Average": "lightgrey",
    "Good": "lightblue",
    "Very Good": "green",
}

COLOR_DICT_FOR_KNOWLEDGE = {
    "I did not improve my knowledge": "orange",
    "I somewhat improved my knowledge": "yellow",
    "I already knew this": "lightgrey",
    "I improved my knowledge": "lightgreen",
    "I hugely improved my knowledge": "green",
}

COLUMN_NAMES_RATING = [
    "variable",
    "Poor",
    "Very Poor",
    "Average",
    "Good",
    "Very Good",
]

COLUMN_NAMES_KNOWLEDGE = [
    "variable",
    "I somewhat improved my knowledge",
    "I did not improve my knowledge",
    "I already knew this",
    "I improved my knowledge",
    "I hugely improved my knowledge",
]


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)
