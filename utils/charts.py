import pandas as pd
from plotly import graph_objects as go

from utils.constants import COLOR_DICT_RATING_SCALE, COLUMN_NAMES_RATING


def divergent_bar_chart(
    data: pd.DataFrame,
    column_names: list[str] = COLUMN_NAMES_RATING,
    colors: dict = COLOR_DICT_RATING_SCALE,
    char_limit: int = 50,
) -> go.Figure:
    data_arranged = data[column_names].copy()

    # Create a new column that is the sum of the right side columns
    data_arranged["right_sum"] = data_arranged[data_arranged.columns[3:]].sum(axis=1)

    # Sort the DataFrame by the new column and then drop it
    data_arranged = data_arranged.sort_values(by="right_sum", ascending=False)
    data_arranged = data_arranged.drop(columns="right_sum")

    # Create the figure
    fig = go.Figure()

    # Add the left bars
    for col in data_arranged.columns[1:3]:
        fig.add_trace(
            go.Bar(
                x=-data_arranged[col].values,
                y=data_arranged["variable"].apply(
                    lambda x: (x[:char_limit] + "...") if len(x) > char_limit else x
                ),
                orientation="h",
                name=col,
                customdata=data_arranged[col],
                hovertemplate="%{y}: %{customdata}",
                marker_color=colors[col],
                text=data_arranged[col],
                textposition="auto",
            )
        )

    # # Add a thick line at x=0
    # fig.add_trace(
    #     go.Scatter(
    #         x=[0, 0],
    #         y=[data_arranged["variable"].iloc[0], data_arranged["variable"].iloc[-1]],
    #         mode="lines",
    #         line=dict(width=2, color="black"),
    #         showlegend=False,
    #     )
    # )

    # Add the right bars
    for col in data_arranged.columns[3:]:
        fig.add_trace(
            go.Bar(
                x=data_arranged[col],
                y=data_arranged["variable"].apply(
                    lambda x: (x[:char_limit] + "...") if len(x) > char_limit else x
                ),
                orientation="h",
                name=col,
                hovertemplate="%{y}: %{x}",
                marker_color=colors[col],
                text=data_arranged[col],
                textposition="auto",
            )
        )

    fig.update_layout(
        barmode="relative",
        yaxis_autorange="reversed",
        bargap=0.01,
        legend_orientation="h",
        legend_x=-0.5,
        legend_y=-0.1,
        legend_xanchor="center",
        title="Divergent Bar Chart",
    )

    return fig


def likert_scale_chart(
    data: pd.DataFrame,
    colors: dict[str, str] = COLOR_DICT_RATING_SCALE,
    char_limit: int = 50,
) -> go.Figure:

    # Create a copy of the DataFrame and add a new column that is the sum of the first two columns
    data_sorted = data.copy()
    data_sorted["sum_first_two"] = data_sorted[data_sorted.columns[3:]].sum(axis=1)

    # Sort the DataFrame by the new column in descending order and then drop it
    data_sorted = data_sorted.sort_values(by="sum_first_two", ascending=False)
    data_sorted = data_sorted.drop(columns="sum_first_two")

    fig = go.Figure()

    for col in data_sorted.columns[1:]:
        fig.add_trace(
            go.Bar(
                x=data_sorted[col],
                y=data_sorted["variable"].apply(
                    lambda x: (x[:char_limit] + "...") if len(x) > char_limit else x
                ),
                orientation="h",
                name=col,
                hovertemplate="%{y}: %{x}",
                marker_color=colors[col],
                text=data_sorted[col],
                textposition="auto",
            )
        )

    fig.update_layout(
        barmode="relative",
        yaxis_autorange="reversed",
        bargap=0.01,
        legend_orientation="h",
        legend_x=-0.5,
        legend_y=-0.1,
        legend_xanchor="center",
        title="Likert Scale Chart",
    )

    return fig


def generate_bar_chart(
    data: pd.DataFrame,
    row_value: str,
    colors: dict[str, str] = COLOR_DICT_RATING_SCALE,
):
    row = data[data["variable"] == row_value].iloc[0]

    fig = go.Figure(
        go.Bar(
            x=row.values[1:],
            y=row.index[1:],
            orientation="h",
            name=row_value,
            hovertemplate="%{y}: %{x}",
            marker_color=[colors[col] for col in row.index[1:]],
        )
    )

    fig.update_layout(
        title=row_value,
        xaxis_title="Count",
        yaxis_title="Category",
        bargap=0.01,
        width=500,
    )

    return fig


def generate_donut_chart(
    data: pd.DataFrame,
    row_value: str,
    width: int = 700,
    colors=COLOR_DICT_RATING_SCALE,
):
    row = data[data["variable"] == row_value].iloc[0]

    fig = go.Figure(
        go.Pie(
            labels=row.index[1:],
            values=row.values[1:],
            text=row.index[1:],
            marker_colors=[colors[col] for col in row.index[1:]],
            hole=0.5,
            hoverinfo="label+percent",
        )
    )

    fig.update_layout(title=row["variable"], showlegend=False, width=width)

    return fig


def generate_cumulative_frequency_chart(
    data: pd.DataFrame, variable_value: str, width: int = 500
):
    row = data[data["variable"] == variable_value].iloc[0]

    fig = go.Figure()

    cumulative_sum = row[1:].cumsum()

    fig.add_trace(
        go.Bar(
            x=cumulative_sum.index,
            y=cumulative_sum.values,
            name=row["variable"],
            width=0.5,
            text=(cumulative_sum.values),
            textposition="outside",
        )
    )

    fig.update_layout(
        yaxis_title="Cumulative Sum",
        title="Cumulative Frequency Chart",
        width=width,
    )

    return fig


def generate_cumulative_percentage_chart(
    data: pd.DataFrame, variable_value: str, width: int = 500
):
    row = data[data["variable"] == variable_value].iloc[0]

    fig = go.Figure()

    cumulative_sum = row[1:].cumsum()
    cumulative_percentage = 100 * cumulative_sum / cumulative_sum.iloc[-1]

    fig.add_trace(
        go.Bar(
            x=cumulative_percentage.index,
            y=cumulative_percentage.values,
            name=row["variable"],
            width=0.5,
            marker_color="green",
        )
    )

    fig.update_layout(
        yaxis_title="Cumulative Percentage (%)",
        title="Cumulative Percentage Chart",
        width=width,
    )

    return fig
