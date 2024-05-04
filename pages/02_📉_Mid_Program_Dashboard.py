import streamlit as st

from utils.charts import (
    divergent_bar_chart,
    generate_bar_chart,
    generate_cumulative_frequency_chart,
    generate_cumulative_percentage_chart,
    generate_donut_chart,
    likert_scale_chart,
)
from utils.constants import (
    COLOR_DICT_FOR_KNOWLEDGE,
    COLUMN_NAMES_KNOWLEDGE,
    MID_PROGRAM_DATA,
    load_data,
)
from utils.data_extraction import instructor_score_strings
from utils.data_preparation import (
    clean_mid_program_data,
    create_pivot_table,
    create_program_exp_pivot_table,
)

st.set_page_config(
    page_title="Mid Program Survey Dashboard",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Mid Program Survey Dashboard")
st.markdown("### This dashboard displays the results of the Mid Program Survey.")


def mid_program_dashboard():
    # load data
    mid_program_data = load_data(MID_PROGRAM_DATA)
    df = clean_mid_program_data(mid_program_data)
    pivot_table = create_pivot_table(df)

    # display data
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "👨‍🏫 Instructor Evaluation",
            "🗂️ Business",
            "👨‍💻 Technology",
            "💹 Marketing & Communications",
            "📍 Soft Skills",
            "❓ Program Aspect Rating",
            "📚 Program Experience",
        ]
    )

    with tab1:
        st.write("## Instructor Evaluation")
        st.divider()

        fellow_evaluation_data = create_pivot_table(
            df[  # data of instructors
                [
                    "Students_Id",
                    "Teaching_Fellow_Evaluation_Abena_Ofori",
                    "Teaching_Fellow_Evaluation_Sandra_Osei",
                    "Teaching_Fellow_Evaluation_Nana_Kofi",
                    "Leading_Fellow_Evaluation_Eugene_Frimpong",
                ]
            ]
        )

        col1, col2 = st.columns(2)

        col1.write("### Eugene Frimpong")
        col1.plotly_chart(
            generate_donut_chart(
                fellow_evaluation_data, "Leading_Fellow_Evaluation_Eugene_Frimpong", 400
            )
        )
        col1.success(
            instructor_score_strings(
                fellow_evaluation_data, "Leading_Fellow_Evaluation_Eugene_Frimpong"
            )
        )

        col2.write("### Abena Ofori")
        col2.plotly_chart(
            generate_donut_chart(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Abena_Ofori", 400
            )
        )
        col2.success(
            instructor_score_strings(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Abena_Ofori"
            )
        )

        st.divider()

        col3, col4 = st.columns(2)

        col3.write("### Sandra Osei")
        col3.plotly_chart(
            generate_donut_chart(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Sandra_Osei", 400
            )
        )
        col3.success(
            instructor_score_strings(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Sandra_Osei"
            )
        )

        col4.write("### Nana Kofi")
        col4.plotly_chart(
            generate_donut_chart(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Nana_Kofi", 400
            )
        )
        col4.success(
            instructor_score_strings(
                fellow_evaluation_data, "Teaching_Fellow_Evaluation_Nana_Kofi"
            )
        )

    with tab2:
        st.write("## Business Skills Survey")
        st.write("### Question:")
        st.write(
            "Evaluate your proficiency and understanding in the following business skill areas"
        )

        st.divider()
        business_data = pivot_table[pivot_table["variable"].str.startswith("Business")]

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in each business skills"
        )

        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(business_data))
        col2.plotly_chart(divergent_bar_chart(business_data))

        st.divider()

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in selected business skills"
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

    with tab3:
        st.write("## Technology Skills Survey")
        st.write("### Question:")
        st.write(
            "Evaluate your proficiency and understanding in the following technology skill areas"
        )

        st.divider()
        technology_data = pivot_table[
            pivot_table["variable"].str.startswith("Technology")
        ]

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in each technology skills"
        )

        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(technology_data))
        col2.plotly_chart(divergent_bar_chart(technology_data))

        st.divider()

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in selected technology skills"
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

    with tab4:
        st.write("## Marketing & Communications")
        st.write("### Question:")
        st.write(
            "Evaluate your proficiency and understanding in the following marketing and communications skill areas"
        )

        st.divider()
        marketing_data = pivot_table[
            pivot_table["variable"].str.startswith("Marketing_Communications")
        ]

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in each marketing and communications skills"
        )

        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(marketing_data))
        col2.plotly_chart(divergent_bar_chart(marketing_data))

        st.divider()

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in selected marketing and communications skills"
        )

        row = st.selectbox(
            "Select a marketing and communications skill",
            marketing_data["variable"],
            key=5,
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(marketing_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(marketing_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected marketing and communications skill."
        )
        row = st.selectbox(
            "Select a marketing and communications skill",
            marketing_data["variable"],
            key=6,
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(marketing_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(marketing_data, row))

    with tab5:
        st.write("## Soft Skills")
        st.write("### Question:")
        st.write(
            "How would you assess your comprehension of the following soft skills at this point?"
        )

        st.divider()
        soft_skills_data = pivot_table[
            pivot_table["variable"].str.startswith("Soft_Skills")
        ]

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in each soft skills"
        )

        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(soft_skills_data))
        col2.plotly_chart(divergent_bar_chart(soft_skills_data))

        st.divider()

        st.write(
            "### The following chart shows the distribution of proficiency of EITs in selected soft skills"
        )

        row = st.selectbox("Select a soft skill", soft_skills_data["variable"], key=7)

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(soft_skills_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(soft_skills_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected soft skill."
        )
        row = st.selectbox("Select a soft skill", soft_skills_data["variable"], key=8)

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(soft_skills_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(generate_cumulative_percentage_chart(soft_skills_data, row))

    with tab6:
        st.write("## Program Aspect Rating")
        st.write("### Question:")
        st.write(
            "Up to this point, how would you rate the following aspects of the EIT Program"
        )

        st.divider()
        program_aspect_data = pivot_table[
            pivot_table["variable"].str.startswith("Program_Aspect_Rating")
        ]

        st.write(
            "### The following chart shows the distribution of ratings of EITs in each program aspect"
        )

        col1, _, col2 = st.columns([1, 0.2, 1])
        col1.plotly_chart(likert_scale_chart(program_aspect_data))
        col2.plotly_chart(divergent_bar_chart(program_aspect_data))

        st.divider()

        st.write(
            "### The following chart shows the distribution of ratings of EITs in selected program aspects"
        )

        row = st.selectbox(
            "Select a program aspect", program_aspect_data["variable"], key=9
        )

        col3, _, col4 = st.columns([1, 0.2, 1])

        col3.write("#### Bar Chart")
        col3.plotly_chart(generate_bar_chart(program_aspect_data, row))

        col4.write("#### Pie Chart")
        col4.plotly_chart(generate_donut_chart(program_aspect_data, row))

        st.divider()

        st.write(
            "### The following charts show the cumulative frequency and percentage of responses for selected program aspect."
        )
        row = st.selectbox(
            "Select a program aspect", program_aspect_data["variable"], key=10
        )

        col5, _, col6 = st.columns([1, 0.2, 1])

        col5.write("#### Cumulative Frequency Chart")
        col5.plotly_chart(generate_cumulative_frequency_chart(program_aspect_data, row))

        col6.write("#### Cumulative Percentage Chart")
        col6.plotly_chart(
            generate_cumulative_percentage_chart(program_aspect_data, row)
        )

    with tab7:
        st.write("## Program Experience Survey")
        st.write(
            "Analysing the survey data on the EIT Program Experience in Technology, Business, and Marketing & Communications"
        )

        program_exp_pivot_table = create_program_exp_pivot_table(
            df[
                ["Students_Id"]
                + [col for col in df.columns if "Program_Experience" in col]
            ]
        )

        tech_program_exp, comms_program_exp, business_program_exp = st.tabs(
            [
                "Technology",
                "Marketing & Communications",
                "Business",
            ]
        )

        with tech_program_exp:
            st.write("### Technology Program Experience")
            st.write("### Question:")
            st.write(
                "Have you experienced an improvement in your skills and knowledge after participating in the sessions on:"
            )

            program_exp_tech_data = program_exp_pivot_table[
                program_exp_pivot_table["variable"].str.startswith(
                    "Program_Experience_Technology"
                )
            ]

            st.divider()

            st.write(
                "### The following chart shows the distribution of responses for selected Experiences in Technology"
            )
            row = st.selectbox(
                "Select a Technology Program Experience",
                program_exp_tech_data["variable"],
                key=13,
            )

            col1, _, col2 = st.columns([1, 0.2, 1])

            col1.write("#### Bar Chart")
            col1.plotly_chart(
                generate_bar_chart(
                    program_exp_tech_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            col2.write("#### Pie Chart")
            col2.plotly_chart(
                generate_donut_chart(
                    program_exp_tech_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            st.divider()

            st.write(
                "### The following charts show the cumulative frequency and percentage of responses for selected Experiences in Technology."
            )

            row = st.selectbox(
                "Select a Technology Program Experience",
                program_exp_tech_data["variable"],
                key=14,
            )
            col3, _, col4 = st.columns([1, 0.2, 1])

            col3.write("#### Cumulative Frequency Chart")
            col3.plotly_chart(
                generate_cumulative_frequency_chart(
                    program_exp_tech_data, row, width=700
                )
            )

            col4.write("#### Cumulative Percentage Chart")
            col4.plotly_chart(
                generate_cumulative_percentage_chart(
                    program_exp_tech_data, row, width=700
                )
            )

            st.divider()

            st.write(
                "### The following charts show the distribution of responses Program Experience in Technology."
            )

            col5, _, col6 = st.columns([1, 0.2, 1])

            col5.plotly_chart(
                likert_scale_chart(
                    program_exp_tech_data,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )
            col6.plotly_chart(
                divergent_bar_chart(
                    program_exp_tech_data,
                    column_names=COLUMN_NAMES_KNOWLEDGE,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )

        with comms_program_exp:
            st.write("### Marketing & Communications Program Experience")
            st.write(
                "The following chart shows the distribution of responses for Marketing & Communications Program Experience"
            )

            program_exp_comms_data = program_exp_pivot_table[
                program_exp_pivot_table["variable"].str.startswith(
                    "Program_Experience_Marketing_Communications"
                )
            ]

            st.divider()

            st.write(
                "### The following chart shows the distribution of responses for selected Experiences in Marketing & Communications"
            )

            row = st.selectbox(
                "Select a Marketing & Communications Program Experience",
                program_exp_comms_data["variable"],
                key=15,
            )

            col1, _, col2 = st.columns([1, 0.2, 1])

            col1.write("#### Bar Chart")
            col1.plotly_chart(
                generate_bar_chart(
                    program_exp_comms_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            col2.write("#### Pie Chart")
            col2.plotly_chart(
                generate_donut_chart(
                    program_exp_comms_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            st.divider()

            st.write(
                "### The following charts show the cumulative frequency and percentage of responses for selected Experiences in Marketing & Communications."
            )

            row = st.selectbox(
                "Select a Marketing & Communications Program Experience",
                program_exp_comms_data["variable"],
                key=16,
            )

            col3, _, col4 = st.columns([1, 0.2, 1])

            col3.write("#### Cumulative Frequency Chart")
            col3.plotly_chart(
                generate_cumulative_frequency_chart(
                    program_exp_comms_data, row, width=700
                )
            )

            col4.write("#### Cumulative Percentage Chart")
            col4.plotly_chart(
                generate_cumulative_percentage_chart(
                    program_exp_comms_data, row, width=700
                )
            )

            st.divider()

            st.write(
                "### The following charts show the distribution of responses Program Experience in Marketing & Communications."
            )

            col5, _, col6 = st.columns([1, 0.2, 1])

            col5.plotly_chart(
                likert_scale_chart(
                    program_exp_comms_data,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )

            col6.plotly_chart(
                divergent_bar_chart(
                    program_exp_comms_data,
                    column_names=COLUMN_NAMES_KNOWLEDGE,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )

        with business_program_exp:
            st.write("### Business Program Experience")
            st.write(
                "The following chart shows the distribution of responses for Business Program Experience"
            )

            program_exp_business_data = program_exp_pivot_table[
                program_exp_pivot_table["variable"].str.startswith(
                    "Program_Experience_Business"
                )
            ]

            st.divider()

            st.write(
                "### The following chart shows the distribution of responses for selected Business Program Experience"
            )

            row = st.selectbox(
                "Select a Business Program Experience",
                program_exp_business_data["variable"],
                key=17,
            )

            col1, _, col2 = st.columns([1, 0.2, 1])

            col1.write("#### Bar Chart")
            col1.plotly_chart(
                generate_bar_chart(
                    program_exp_business_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            col2.write("#### Pie Chart")
            col2.plotly_chart(
                generate_donut_chart(
                    program_exp_business_data, row, colors=COLOR_DICT_FOR_KNOWLEDGE
                )
            )

            st.divider()

            st.write(
                "### The following charts show the cumulative frequency and percentage of responses for selected Business Program Experience."
            )

            row = st.selectbox(
                "Select a Business Program Experience",
                program_exp_business_data["variable"],
                key=18,
            )

            col3, _, col4 = st.columns([1, 0.2, 1])

            col3.write("#### Cumulative Frequency Chart")
            col3.plotly_chart(
                generate_cumulative_frequency_chart(
                    program_exp_business_data, row, width=700
                )
            )

            col4.write("#### Cumulative Percentage Chart")
            col4.plotly_chart(
                generate_cumulative_percentage_chart(
                    program_exp_business_data, row, width=700
                )
            )

            st.divider()

            st.write(
                "### The following charts show the distribution of responses Program Experience in Business."
            )

            col5, _, col6 = st.columns([1, 0.2, 1])

            col5.plotly_chart(
                likert_scale_chart(
                    program_exp_business_data,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )

            col6.plotly_chart(
                divergent_bar_chart(
                    program_exp_business_data,
                    column_names=COLUMN_NAMES_KNOWLEDGE,
                    colors=COLOR_DICT_FOR_KNOWLEDGE,
                )
            )


if __name__ == "__main__":
    mid_program_dashboard()
