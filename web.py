import streamlit as st

def disc_test():
    st.title("DISC Personality Test")

    questions = {
        "Dominance": [
            "I enjoy taking charge and leading others.",
            "I prefer making decisions independently rather than consulting others.",
            "I am assertive and direct in my communication style.",
            "I strive to achieve my goals, even if it means being assertive."
        ],
        "Influence": [
            "I enjoy socializing and networking with others.",
            "I am enthusiastic and outgoing in social situations.",
            "I enjoy motivating and inspiring others.",
            "I am often described as charismatic or charming by others."
        ],
        "Steadiness": [
            "I value stability and predictability in my life.",
            "I am patient and understanding with others.",
            "I am calm and composed under pressure.",
            "I have a strong sense of loyalty to my friends and colleagues."
        ],
        "Conscientiousness": [
            "I pay attention to detail and strive for accuracy in my work.",
            "I prefer following established procedures and guidelines.",
            "I enjoy planning and organizing my work schedule.",
            "I am reliable and can be trusted to meet deadlines."
        ]
    }

    scores = {}
    for dimension, dimension_questions in questions.items():
        st.subheader(dimension)
        dimension_score = 0
        for i, question in enumerate(dimension_questions):
            st.write(f"{i + 1}. {question}")
            score = st.radio("Select your answer:", options=[1, 2, 3, 4, 5], key=f"{dimension}-{i}")
            dimension_score += score
        scores[dimension] = dimension_score

    return scores

def generate_report(scores):
    st.title("DISC Test Report")

    st.write("### Personality Scores:")
    for dimension, score in scores.items():
        st.write(f"- {dimension}: {score}")

    st.write("### Detailed Evaluation:")
    # Perform detailed evaluation based on scores (you can customize this based on your criteria)

    st.write("### Profession Best Fit:")
    # Suggest professions based on scores (you can customize this based on your criteria)

def main():
    st.set_page_config(page_title="DISC Test", layout="wide")
    st.sidebar.title("DISC Test")

    page = st.sidebar.radio("Select Page:", options=["Test", "Report"])

    if page == "Test":
        scores = disc_test()
        st.sidebar.button("Generate Report", on_click=lambda: st.experimental_set_query_params(report=True, **scores))
    elif page == "Report":
        scores = {key: int(value) for key, value in st.experimental_get_query_params().items()}
        generate_report(scores)

if __name__ == "__main__":
    main()
