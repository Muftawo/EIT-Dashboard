import pandas as pd
from textblob import TextBlob


def get_cell_value(
    data: pd.DataFrame,
    target_col_name: str,
    row_reference_value: str,
    row_reference_col_name: str = "variable",
):

    cell_value = data.loc[
        data[row_reference_col_name] == row_reference_value, target_col_name
    ]

    return cell_value.item()


def instructor_score_strings(data: pd.DataFrame, instructor_row_value: str):
    return f"""
            **Very Good:**      {get_cell_value(
                data,
                "Very Good",
                instructor_row_value,
            )},
            **Good:**           {get_cell_value(
                data,
                "Good",
                instructor_row_value,
            )},\n
            **Average:**        {get_cell_value(
                data,
                "Average",
                instructor_row_value,
            )},\n
            **Poor:**           {get_cell_value(
                data,
                "Poor",
                instructor_row_value,
            )},
            **Very Poor:**      {get_cell_value(
                data,
                "Very Poor",
                instructor_row_value,
            )}
            """


def get_sentiment(text: str):
    return TextBlob(text).sentiment.polarity
