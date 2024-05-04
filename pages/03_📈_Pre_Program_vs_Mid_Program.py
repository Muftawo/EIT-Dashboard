import streamlit as st

from utils.charts import (
    divergent_bar_chart,
    generate_cumulative_frequency_chart,
    generate_cumulative_percentage_chart,
    generate_donut_chart,
    likert_scale_chart,
)
from utils.constants import MID_PROGRAM_DATA, PRE_PROGRAM_DATA, load_data
from utils.data_preparation import (
    clean_mid_program_data,
    clean_pre_program_data,
    create_pivot_table,
)

st.set_page_config(
    page_title="Pre Program vs Mid Program Survey Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Pre Program vs Mid Program Survey Dashboard")
st.markdown(
    "#### A Comparison between Pre-Program Survey and Mid Program Survey Response"
)


def comparison_view():
    pre_program_data = load_data(PRE_PROGRAM_DATA)
    mid_program_data = load_data(MID_PROGRAM_DATA)

    pre_df = clean_pre_program_data(pre_program_data)
    mid_df = clean_mid_program_data(mid_program_data)

    pre_pivot_table = create_pivot_table(pre_df)
    mid_pivot_table = create_pivot_table(mid_df)

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🗂️ Business",
            "👨‍💻 Technology",
            "💹 Marketing & Communications",
            "📍 Soft Skills",
        ]
    )

    with tab1:
        pre_business_data = pre_pivot_table[
            pre_pivot_table["variable"].str.startswith("Business")
        ]

        mid_business_data = mid_pivot_table[
            mid_pivot_table["variable"].str.startswith("Business")
        ]

        st.write("## Business Skill Comparison")
        st.divider()

        st.write("### Business Comparison Using Likert Scale Charts Comparison")
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(pre_business_data))
        col2.plotly_chart(likert_scale_chart(mid_business_data))

        st.divider()

        st.write("### Business Comparison Using Donut Charts Comparison")
        col3, _, col4 = st.columns([1, 0.2, 1])
        row = col3.selectbox("Select a row", pre_business_data["variable"], key=1)
        col3.plotly_chart(generate_donut_chart(pre_business_data, row))

        row = col4.selectbox("Select a row", mid_business_data["variable"], key=2)
        col4.plotly_chart(generate_donut_chart(mid_business_data, row))

        st.divider()

        st.write("### Business Comparison Using Cummulative Charts Comparison")
        col5, _, col6 = st.columns([1, 0.2, 1])
        row = col5.selectbox("Select a row", pre_business_data["variable"], key=3)
        col5.plotly_chart(generate_cumulative_percentage_chart(pre_business_data, row))
        col5.plotly_chart(generate_cumulative_frequency_chart(pre_business_data, row))

        row = col6.selectbox("Select a row", mid_business_data["variable"], key=4)
        col6.plotly_chart(generate_cumulative_percentage_chart(mid_business_data, row))
        col6.plotly_chart(generate_cumulative_frequency_chart(mid_business_data, row))

        st.divider()

    with tab2:
        pre_technology_data = pre_pivot_table[
            pre_pivot_table["variable"].str.startswith("Technology")
        ]

        mid_technology_data = mid_pivot_table[
            mid_pivot_table["variable"].str.startswith("Technology")
        ]

        st.write("## Technology Skill Comparison")
        st.divider()

        st.write("### Technology Comparison Using Likert Scale Charts Comparison")
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(pre_technology_data))
        col2.plotly_chart(likert_scale_chart(mid_technology_data))

        st.divider()

        st.write("### Technology Comparison Using Donut Charts Comparison")
        col3, _, col4 = st.columns([1, 0.2, 1])
        row = col3.selectbox("Select a row", pre_technology_data["variable"], key=5)
        col3.plotly_chart(generate_donut_chart(pre_technology_data, row))

        row = col4.selectbox("Select a row", mid_technology_data["variable"], key=6)
        col4.plotly_chart(generate_donut_chart(mid_technology_data, row))

        st.divider()

        st.write("### Technology Comparison Using Cummulative Charts Comparison")
        col5, _, col6 = st.columns([1, 0.2, 1])
        row = col5.selectbox("Select a row", pre_technology_data["variable"], key=7)
        col5.plotly_chart(
            generate_cumulative_percentage_chart(pre_technology_data, row)
        )
        col5.plotly_chart(generate_cumulative_frequency_chart(pre_technology_data, row))

        row = col6.selectbox("Select a row", mid_technology_data["variable"], key=8)
        col6.plotly_chart(
            generate_cumulative_percentage_chart(mid_technology_data, row)
        )
        col6.plotly_chart(generate_cumulative_frequency_chart(mid_technology_data, row))

        st.divider()

    with tab3:
        pre_marketing_data = pre_pivot_table[
            pre_pivot_table["variable"].str.startswith("Communication")
        ]

        mid_marketing_data = mid_pivot_table[
            mid_pivot_table["variable"].str.startswith("Marketing_Communications")
        ]

        st.write("## Marketing & Communication Skill Comparison")
        st.divider()

        st.write(
            "### Marketing & Communication Comparison Using Likert Scale Charts Comparison"
        )
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(pre_marketing_data))
        col2.plotly_chart(likert_scale_chart(mid_marketing_data))

        st.divider()

        st.write(
            "### Marketing & Communication Comparison Using Donut Charts Comparison"
        )
        col3, _, col4 = st.columns([1, 0.2, 1])
        row = col3.selectbox("Select a row", pre_marketing_data["variable"], key=9)
        col3.plotly_chart(generate_donut_chart(pre_marketing_data, row))

        row = col4.selectbox("Select a row", mid_marketing_data["variable"], key=10)
        col4.plotly_chart(generate_donut_chart(mid_marketing_data, row))

        st.divider()

        st.write(
            "### Marketing & Communication Comparison Using Cummulative Charts Comparison"
        )
        col5, _, col6 = st.columns([1, 0.2, 1])
        row = col5.selectbox("Select a row", pre_marketing_data["variable"], key=11)
        col5.plotly_chart(generate_cumulative_percentage_chart(pre_marketing_data, row))
        col5.plotly_chart(generate_cumulative_frequency_chart(pre_marketing_data, row))

        row = col6.selectbox("Select a row", mid_marketing_data["variable"], key=12)
        col6.plotly_chart(generate_cumulative_percentage_chart(mid_marketing_data, row))
        col6.plotly_chart(generate_cumulative_frequency_chart(mid_marketing_data, row))

        st.divider()

    with tab4:
        pre_soft_skill_data = pre_pivot_table[
            pre_pivot_table["variable"].str.startswith("Soft_Skill")
        ]

        mid_soft_skill_data = mid_pivot_table[
            mid_pivot_table["variable"].str.startswith("Soft_Skill")
        ]

        st.write("## Soft Skill Comparison")
        st.divider()

        st.write("### Soft Skill Comparison Using Likert Scale Charts Comparison")
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(pre_soft_skill_data))
        col2.plotly_chart(likert_scale_chart(mid_soft_skill_data))

        st.divider()

        st.write("### Soft Skill Comparison Using Donut Charts Comparison")
        col3, _, col4 = st.columns([1, 0.2, 1])
        row = col3.selectbox("Select a row", pre_soft_skill_data["variable"], key=13)
        col3.plotly_chart(generate_donut_chart(pre_soft_skill_data, row))

        row = col4.selectbox("Select a row", mid_soft_skill_data["variable"], key=14)
        col4.plotly_chart(generate_donut_chart(mid_soft_skill_data, row))

        st.divider()

        st.write("### Soft Skill Comparison Using Cummulative Charts Comparison")
        col5, _, col6 = st.columns([1, 0.2, 1])
        row = col5.selectbox("Select a row", pre_soft_skill_data["variable"], key=15)
        col5.plotly_chart(
            generate_cumulative_percentage_chart(pre_soft_skill_data, row)
        )
        col5.plotly_chart(generate_cumulative_frequency_chart(pre_soft_skill_data, row))

        row = col6.selectbox("Select a row", mid_soft_skill_data["variable"], key=16)
        col6.plotly_chart(
            generate_cumulative_percentage_chart(mid_soft_skill_data, row)
        )
        col6.plotly_chart(generate_cumulative_frequency_chart(mid_soft_skill_data, row))

        st.divider()


if __name__ == "__main__":
    comparison_view()
