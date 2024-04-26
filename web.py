class DISCTest:
    def __init__(self):
        self.questions = {
            "Dominance": [
                "I enjoy taking charge and leading others.",
                "I often find myself in leadership roles without actively seeking them.",
                "I prefer making decisions independently rather than consulting others.",
                "I am assertive and direct in my communication style.",
                "I feel comfortable expressing my opinions, even if they differ from others.",
                "I enjoy challenges and am motivated by overcoming obstacles.",
                "I strive to achieve my goals, even if it means being assertive.",
                "I have a competitive nature and enjoy competing to win.",
                "I am not afraid to confront others when necessary.",
                "I enjoy taking risks and exploring new opportunities.",
                "I prefer to lead rather than follow in group settings.",
                "I feel frustrated when others are indecisive or hesitant.",
                "I am comfortable delegating tasks to others and trusting them to get the job done.",
                "I am not afraid to speak up and advocate for myself and others.",
                "I enjoy being in control of situations and outcomes."
            ],
            "Influence": [
                "I enjoy socializing and networking with others.",
                "I am enthusiastic and outgoing in social situations.",
                "I prefer working in teams and collaborating with others.",
                "I enjoy motivating and inspiring others.",
                "I am good at persuading others to see my point of view.",
                "I thrive in social environments and enjoy being the center of attention.",
                "I am often described as charismatic or charming by others.",
                "I enjoy sharing ideas and brainstorming with others.",
                "I am skilled at building rapport and forming relationships with diverse individuals.",
                "I am comfortable speaking in front of large groups.",
                "I often take on the role of mediator or peacemaker in conflicts.",
                "I enjoy participating in group activities and social events.",
                "I am naturally outgoing and find it easy to strike up conversations with strangers.",
                "I am persuasive and can influence others to take action.",
                "I enjoy being involved in community or social initiatives."
            ],
            "Steadiness": [
                "I value stability and predictability in my life.",
                "I am patient and understanding with others.",
                "I prefer to avoid conflicts and maintain harmony in relationships.",
                "I am reliable and consistent in my actions.",
                "I enjoy supporting and helping others in times of need.",
                "I am calm and composed under pressure.",
                "I have a strong sense of loyalty to my friends and colleagues.",
                "I prefer a steady and predictable work environment.",
                "I tend to stay calm and level-headed in stressful situations.",
                "I am known for my patience and ability to listen attentively.",
                "I value traditions and routines in my daily life.",
                "I avoid making hasty decisions and prefer to think things through carefully.",
                "I enjoy building long-term relationships with others.",
                "I am dependable and can be counted on to fulfill my commitments.",
                "I prefer a work environment where I can focus on one task at a time."
            ],
            "Conscientiousness": [
                "I pay attention to detail and strive for accuracy in my work.",
                "I am organized and methodical in my approach to tasks.",
                "I prefer following established procedures and guidelines.",
                "I am focused and disciplined in achieving my objectives.",
                "I take pride in completing tasks thoroughly and efficiently.",
                "I am self-disciplined and have high standards for myself.",
                "I enjoy planning and organizing my work schedule.",
                "I am reliable and can be trusted to meet deadlines.",
                "I prefer to have a clear plan before starting a project.",
                "I enjoy learning and continuously strive to improve my skills.",
                "I am conscientious about my work and pay attention to quality.",
                "I am detail-oriented and notice errors or inconsistencies easily.",
                "I dislike leaving tasks unfinished and prefer closure.",
                "I enjoy organizing information and creating structured systems.",
                "I am thorough in my approach to problem-solving and decision-making."
            ]
        }

    def take_test(self):
        scores = {}
        for dimension, dimension_questions in self.questions.items():
            print(f"\n{dimension} Questions:")
            dimension_score = 0
            for question in dimension_questions:
                print(question)
                score = int(input("Rating (1-5): "))
                dimension_score += score
            scores[dimension] = dimension_score
        return scores

    def interpret_scores(self, scores):
        personality_profile = {}
        for dimension, score in scores.items():
            if score <= 45:
                personality_profile[dimension] = "Low"
            elif 45 < score <= 75:
                personality_profile[dimension] = "Moderate"
            else:
                personality_profile[dimension] = "High"
        return personality_profile

    def generate_report(self, scores, personality_profile):
        print("\n--- Personality Profile ---")
        for dimension, score in scores.items():
            print(f"{dimension}: {score} ({personality_profile[dimension]} level)")

    def suggest_profession(self, personality_profile):
        professions = {
            "Dominance": {
                "Low": "Team Member, Customer Service Representative",
                "Moderate": "Project Manager, Sales Manager",
                "High": "Entrepreneur, CEO"
            },
            "Influence": {
                "Low": "Accountant, Data Analyst",
                "Moderate": "Marketing Specialist, Public Relations Manager",
                "High": "Sales Executive, Event Planner"
            },
            "Steadiness": {
                "Low": "Stock Trader, Real Estate Agent",
                "Moderate": "Human Resources Manager, Counselor",
                "High": "Nurse, Social Worker"
            },
            "Conscientiousness": {
                "Low": "Artist, Tour Guide",
                "Moderate": "Project Coordinator, Quality Assurance Specialist",
                "High": "Financial Analyst, Research Scientist"
            }
        }
        print("\n--- Recommended Professions ---")
        for dimension, level in personality_profile.items():
            print(f"{dimension}: {professions[dimension][level]}")

def main():
    test = DISCTest()
    print("Welcome to the DISC Personality Test!")
    print("Answer each question on a scale from 1 to 5.")
    scores = test.take_test()
    personality_profile = test.interpret_scores(scores)
    test.generate_report(scores, personality_profile)
    test.suggest_profession(personality_profile)

if __name__ == "__main__":
    main()
