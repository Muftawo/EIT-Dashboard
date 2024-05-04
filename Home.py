import streamlit as st

from utils.charts import (
    divergent_bar_chart,
    generate_bar_chart,
    generate_cumulative_frequency_chart,
    generate_cumulative_percentage_chart,
    generate_donut_chart,
    likert_scale_chart,
)
from utils.constants import PRE_PROGRAM_DATA, load_data
from utils.data_extraction import get_sentiment
from utils.data_preparation import clean_pre_program_data, create_pivot_table

st.set_page_config(
    page_title="EIT Dashboard",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("EIT SURVEY DASHBOARD")
st.markdown("### Welcome to the EIT Survey Dashboard! 🚀")


def pre_program_dashboard():
    # load data
    pre_program_data = load_data(PRE_PROGRAM_DATA)
    df = clean_pre_program_data(pre_program_data)
    pivot_table = create_pivot_table(df)

    # display charts
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🗂️ Business",
            "👨‍💻 Technology",
            "💹 Marketing & Communications",
            "📍 Soft Skills",
            "📚 Program Experience",
            "📣 Open Ended Questions",
        ]
    )

    with tab1:
        st.write("## Business Skills Survey")
        st.write("### Question:")
        st.write(
            "Before the EIT Program, how would you rate your proficiency in the following business skills?",
        )
        st.divider()

        business_data = pivot_table[pivot_table["variable"].str.startswith("Business")]

        st.write(
            "### The following charts show the distribution of responses for each business skill."
        )
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(business_data))
        col2.plotly_chart(divergent_bar_chart(business_data))

        st.divider()

        st.write(
            "### The following charts show the distribution of responses for selected business skill."
        )
        row = st.selectbox("Select a business skill", business_data["variable"], key=1)

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(business_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(business_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected business skill."
        )
        row = st.selectbox("Select a business skill", business_data["variable"], key=2)

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(business_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(business_data, row))

    with tab2:
        st.write("## Technology Skills Survey")
        st.write("### Question:")
        st.write(
            "Before the EIT Program, how would you rate your proficiency in the following technology skills?"
        )
        st.divider()

        technology_data = pivot_table[
            pivot_table["variable"].str.startswith("Technology")
        ]

        col1, _, col2 = st.columns([1, 0.2, 1])

        col1.plotly_chart(likert_scale_chart(technology_data))
        col2.plotly_chart(divergent_bar_chart(technology_data))

        st.divider()

        st.write(
            "### The following charts show the distribution of responses for selected technology skill."
        )
        row = st.selectbox(
            "Select a technology skill", technology_data["variable"], key=3
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(technology_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(technology_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected technology skill."
        )
        row = st.selectbox(
            "Select a technology skill", technology_data["variable"], key=4
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(technology_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(technology_data, row))

    with tab3:
        st.write("## Marketing & Communications Skills Survey")
        st.write("### Question:")
        st.write(
            "Before the EIT Program, how would you rate your proficiency in the following marketing & communications skills?"
        )
        st.divider()

        marketing_data = pivot_table[
            pivot_table["variable"].str.startswith("Communication")
        ]

        st.write(
            "### The following charts show the distribution of responses for each communication skill."
        )
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(marketing_data))
        col2.plotly_chart(divergent_bar_chart(marketing_data))

        st.divider()

        st.write(
            "### The following charts show the distribution of responses for selected communication skill."
        )
        row = st.selectbox(
            "Select a communication skill", marketing_data["variable"], key=5
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(marketing_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(marketing_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected communication skill."
        )
        row = st.selectbox(
            "Select a communication skill", marketing_data["variable"], key=6
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(marketing_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(marketing_data, row))

    with tab4:
        st.write("## Soft Skills Survey")
        st.write("### Question:")
        st.write(
            "Before the EIT Program, how would you rate your proficiency in the following soft skills areas?",
        )
        st.divider()

        soft_skills_data = pivot_table[
            pivot_table["variable"].str.startswith("Soft_Skill")
        ]

        st.write(
            "### The following charts show the distribution of responses for each soft skill."
        )
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(soft_skills_data))
        col2.plotly_chart(divergent_bar_chart(soft_skills_data))

        st.divider()

        st.write(
            "### The following charts show the distribution of responses for selected business skill."
        )
        row = st.selectbox(
            "Select a business skill", soft_skills_data["variable"], key=7
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(soft_skills_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(soft_skills_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected business skill."
        )
        row = st.selectbox(
            "Select a business skill", soft_skills_data["variable"], key=8
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(soft_skills_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(soft_skills_data, row))

    with tab5:
        st.write("## Program Experience Survey")
        st.write("### Question:")
        st.write("How would you evaluate the following components of the program?")
        st.divider()

        program_experience_data = pivot_table[
            pivot_table["variable"].str.startswith("Program")
        ]

        st.write(
            "### The following charts show the distribution of responses for each program experience."
        )
        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(program_experience_data))
        col2.plotly_chart(divergent_bar_chart(program_experience_data))

        st.divider()

        st.write(
            "### The following charts show the distribution of responses for selected program experience."
        )
        row = st.selectbox(
            "Select a program experience", program_experience_data["variable"], key=9
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(program_experience_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(program_experience_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected program experience."
        )
        row = st.selectbox(
            "Select a program experience", program_experience_data["variable"], key=10
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(
            generate_cumulative_frequency_chart(program_experience_data, row)
        )

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(
            generate_cumulative_percentage_chart(program_experience_data, row)
        )

    with tab6:
        st.write("## Open Ended Questions")
        st.write("### If any, what further assistance would you have preferred?")
        open_ended_response_data = df[
            "If_any_what_further_assistance_would_you_have_preferred"
        ]

        # remove missing values from the open ended response data
        open_ended_response_data = open_ended_response_data.dropna()

        col1, col2, col3 = st.columns([1, 1, 1])
        col1.markdown("### Positive Sentiments")
        col2.markdown("### Neutral Sentiments")
        col3.markdown("### Negative Sentiments")

        # display the open ended responses as comments in a card layout
        for _, response in enumerate(open_ended_response_data, 1):
            sentiment = get_sentiment(response)

            if sentiment > 0:
                col1.success(f"{response}\n\n**Sentiment Score: {sentiment:.2f}**")

            elif sentiment < 0:
                col3.error(f"{response}\n\n**Sentiment Score: {sentiment:.2f}**")

            else:
                col2.warning(f"{response}\n\n**Sentiment Score: {sentiment:.2f}**")


if __name__ == "__main__":
    pre_program_dashboard()
