import pandas as pd


def clean_pre_program_data(df: pd.DataFrame) -> pd.DataFrame:
    new_columns = [
        col.replace(
            "Before the EIT program, how would you rate your skills and knowledge in these areas?",
            "",
        )
        .replace(
            "How would you rate your proficiency in the following soft skills?",
            "Soft_Skills",
        )
        .replace(
            "How would you evaluate the following components of the program?",
            "Program_Evaluation",
        )
        .replace("[", "")
        .replace("]", "")
        .replace(")", "")
        .replace("(", "")
        .replace(",", "")
        .replace("-", "_")
        .replace("?", "")
        .replace("&", "")
        .replace("    ", " ")
        .replace("   ", " ")
        .replace("  ", " ")
        .replace(" ", "_")
        for col in df.columns
    ]

    df.rename(columns=dict(zip(df.columns, new_columns)), inplace=True)

    return df


def clean_mid_program_data(df: pd.DataFrame) -> pd.DataFrame:
    new_columns = [
        col.replace("Student_Id", "Students_Id")
        .replace("Student Id", "Students_Id")
        .replace(" Evaluate your proficiency and understanding in the area of", "")
        .replace(
            "Have you experienced an improvement in your skills and knowledge after participating in the sessions on",
            " Program Experience ",
        )
        .replace(
            "How would you assess your comprehension of the following soft skills at this point?",
            "Soft_Skills",
        )
        .replace(
            "How would you evaluate the teaching fellows who have been conducting the sessions so far?",
            "Teaching Fellow Evaluation",
        )
        .replace(
            "How would you assess the teaching fellows leading the sessions so far?",
            "Leading Fellow Evaluation",
        )
        .replace(
            "How would you evaluate the teaching fellows who have been conducting the sessions so far?",
            "Teaching Fellow Evaluation",
        )
        .replace(
            "Up to this point, how would you rate the following aspects of the EIT Program",
            "Program Aspect Rating",
        )
        .replace("[", "")
        .replace("]", "")
        .replace(")", "")
        .replace("(", "")
        .replace(",", "")
        .replace("-", "_")
        .replace("?", "")
        .replace("&", "")
        .replace("    ", " ")
        .replace("   ", " ")
        .replace("  ", " ")
        .replace(" ", "_")
        .replace("Business_Program_Experience", "Program_Experience_Business")
        .replace(
            "Marketing_Communications_Program_Experience",
            "Program_Experience_Marketing_Communications",
        )
        .replace("Technology_Program_Experience", "Program_Experience_Technology")
        .replace(
            "Program_Aspect_RatePeer_Learning_and_Collaboration",
            "Program_Aspect_Rate_Peer_Learning_and_Collaboration",
        )
        .replace(
            "RatingPeer",
            "Rating_Peer",
        )
        .replace("Program_Aspect_Rate", "Program_Aspect_Rating")
        for col in df.columns
    ]

    df.rename(columns=dict(zip(df.columns, new_columns)), inplace=True)

    return df


def create_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    df_transformed: pd.DataFrame = pd.pivot_table(
        df.melt(id_vars="Students_Id"),
        index="variable",
        columns="value",
        aggfunc="size",
        fill_value=0,
    )

    df_clean = df_transformed.reset_index()

    if "Very Poor" not in df_clean.columns:
        df_clean["Very Poor"] = 0

    if "Poor" not in df_clean.columns:
        df_clean["Poor"] = 0

    if "Average" not in df_clean.columns:
        df_clean["Average"] = 0

    if "Good" not in df_clean.columns:
        df_clean["Good"] = 0

    if "Very Good" not in df_clean.columns:
        df_clean["Very Good"] = 0

    df_clean = df_clean[
        [
            "variable",
            "Very Poor",
            "Poor",
            "Average",
            "Good",
            "Very Good",
        ]
    ]

    return df_clean


def create_program_exp_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    df_transformed: pd.DataFrame = pd.pivot_table(
        df.melt(id_vars="Students_Id"),
        index="variable",
        columns="value",
        aggfunc="size",
        fill_value=0,
    )

    df_clean = df_transformed.reset_index()

    if "I did not improve my knowledge" not in df_clean.columns:
        df_clean["I did not improve my knowledge"] = 0

    if "I somewhat improved my knowledge" not in df_clean.columns:
        df_clean["I somewhat improved my knowledge"] = 0

    if "I already knew this" not in df_clean.columns:
        df_clean["I already knew this"] = 0

    if "I improved my knowledge" not in df_clean.columns:
        df_clean["I improved my knowledge"] = 0

    if "I hugely improved my knowledge" not in df_clean.columns:
        df_clean["I hugely improved my knowledge"] = 0

    df_clean = df_clean[
        [
            "variable",
            "I did not improve my knowledge",
            "I somewhat improved my knowledge",
            "I already knew this",
            "I improved my knowledge",
            "I hugely improved my knowledge",
        ]
    ]

    return df_clean

