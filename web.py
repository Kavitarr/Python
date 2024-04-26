import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(scores):
    email = "your_email@gmail.com"  # Your email address
    password = "your_password"      # Your email password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = "kavitarai.99@gmail.com"
    msg['Subject'] = "Occupational Interest Assessment Results"

    body = f"Realistic: {scores['Realistic']}\nInvestigative: {scores['Investigative']}\nArtistic: {scores['Artistic']}\nSocial: {scores['Social']}\nEnterprising: {scores['Enterprising']}"
    msg.attach(MIMEText(body, 'plain'))

    server.send_message(msg)
    server.quit()

def main():
    st.title("Occupational Interest Assessment")

    st.write("Instructions: Please answer the following questions based on how strongly you agree or disagree.")
    st.write("1. Strongly Disagree\n2. Disagree\n3. Neutral\n4. Agree\n5. Strongly Agree")

    questions = {
        "Realistic (Doer)": [
            "I enjoy working with my hands to create or fix things.",
            "I prefer outdoor activities over indoor activities.",
            "I like to solve practical problems using tools or equipment.",
            "I am interested in careers that involve physical activity or manual labor.",
            "I prefer learning through hands-on experiences rather than reading or listening.",
            "I am good at building or repairing things.",
            "I enjoy working with machines or mechanical systems.",
            "I like jobs that have clear and tangible results.",
            "I am interested in careers related to agriculture, construction, or mechanics.",
            "I enjoy physical challenges and sports."
        ],
        "Investigative (Thinker)": [
            "I am curious about how things work and enjoy figuring out puzzles.",
            "I enjoy analyzing data or information to find patterns or solutions.",
            "I prefer reading and researching to discover new information.",
            "I like to solve complex problems using logic and reasoning.",
            "I enjoy working independently to investigate questions or hypotheses.",
            "I am good at understanding abstract concepts or theories.",
            "I enjoy conducting experiments or conducting research studies.",
            "I like to explore new ideas or theories.",
            "I am interested in careers related to science, technology, or research.",
            "I enjoy learning about how the world works through observation and analysis."
        ],
        "Artistic (Creator)": [
            "I enjoy expressing myself through creative outlets like art or music.",
            "I prefer jobs that allow me to use my imagination and creativity.",
            "I like to think outside the box and come up with innovative ideas.",
            "I enjoy creating visual or performing arts.",
            "I am good at thinking of unique solutions to problems.",
            "I like jobs that allow me to express my individuality and originality.",
            "I enjoy activities like drawing, painting, or writing.",
            "I like to design or create things that are visually appealing.",
            "I am interested in careers related to design, media, or entertainment.",
            "I enjoy attending artistic events or performances."
        ],
        "Social (Helper)": [
            "I enjoy working with people and helping them solve problems.",
            "I prefer jobs that involve interacting with others and building relationships.",
            "I am good at listening to others and offering support or advice.",
            "I like to collaborate with others to achieve common goals.",
            "I enjoy teaching, mentoring, or coaching others.",
            "I am interested in understanding people's emotions and motivations.",
            "I like to volunteer or participate in community service activities.",
            "I enjoy working in groups or teams to accomplish tasks.",
            "I am interested in careers related to counseling, healthcare, or education.",
            "I feel fulfilled when I can make a positive impact on others' lives."
        ],
        "Enterprising (Persuader)": [
            "I enjoy taking initiative and leading others towards a common goal.",
            "I prefer jobs that involve taking risks and making decisions.",
            "I am good at persuading others to see my point of view or take action.",
            "I like to set goals and work towards achieving them.",
            "I enjoy networking and building connections with others.",
            "I am interested in starting my own business or organization.",
            "I like to negotiate and influence outcomes in my favor.",
            "I enjoy competing with others to achieve success.",
            "I am interested in careers related to sales, marketing, or entrepreneurship.",
            "I feel energized when I can take charge and make things happen."
        ]
    }

    answers = {}
    for dimension, dimension_questions in questions.items():
        st.subheader(dimension)
        for i, question in enumerate(dimension_questions, start=1):
            answer = st.radio(f"{i}. {question}", options=[1, 2, 3, 4, 5], key=f"{dimension}-{i}")
            answers[f"{dimension}-{i}"] = answer

    if st.button("Submit"):
    scores = {
        "Realistic": sum(answers[f"Realistic-{i}"] for i in range(1, 11)),
        "Investigative": sum(answers[f"Investigative-{i}"] for i in range(1, 11)),
        "Artistic": sum(answers[f"Artistic-{i}"] for i in range(1, 11)),
        "Social": sum(answers[f"Social-{i}"] for i in range(1, 11)),
        "Enterprising": sum(answers[f"Enterprising-{i}"] for i in range(1, 11)),
    }
    send_email(scores)
    st.success("Your assessment has been submitted. Results will be sent to your email.")
if __name__ == "__main__":
    main()
