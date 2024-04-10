import app
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

def page_1():
    
    st.title("Comprehension Check in Multiple Languages")

    # Define passages and questions in multiple languages
    passage = '''The internet has revolutionized the way we communicate, work, and access information. 
    It has its origins in the 1960s when the United States Department of Defense developed ARPANET, 
    a precursor to the modern internet. ARPANET allowed multiple computers to communicate on a single network, 
    laying the groundwork for what would become the internet. 
    In the 1980s, the National Science Foundation created NSFNET, a network that connected universities and 
    research institutions, further expanding the internet's reach. The development of the World Wide Web in the 
    early 1990s by Tim Berners-Lee made it possible for users to access websites and navigate the internet easily. 
    Today, the internet is an integral part of daily life, connecting billions of people around the world and 
    enabling a vast array of online activities.
    '''
    
    # Language selection
    to_language = st.selectbox("Select Language", list(LANGUAGES.values()))
    result_passage = app.translator_function(passage, "en", app.language_mapping[to_language]).text

    questions_answers = {
    "questions": [
                {
            "question": "What was ARPANET's primary purpose?",
            "choices": [
                "Military communication",
                "Academic research",
                "Commercial transactions",
                "Entertainment"
            ],
            "answer": "Military communication"
        },
        {
            "question": "Who developed the World Wide Web?",
            "choices": [
                "Bill Gates",
                "Steve Jobs",
                "Tim Berners-Lee",
                "Mark Zuckerberg"
            ],
            "answer": "Tim Berners-Lee"
        },
        {
            "question": "What is the internet's role in daily life today?",
            "choices": [
                "Connecting people globally",
                "Storing personal files",
                "Playing video games",
                "All of the above"
            ],
            "answer": "Connecting people globally"
        },
        {
            "question": "Which organization developed ARPANET?",
            "choices": [
                "IBM",
                "Microsoft",
                "Apple",
                "United States Department of Defense"
            ],
            "answer": "United States Department of Defense"
        },
        {
            "question": "What was the purpose of NSFNET?",
            "choices": [
                "Military communication",
                "Academic research",
                "Commercial transactions",
                "Entertainment"
            ],
            "answer": "Academic research"
        },
        {
            "question": "Which development made it easier for users to access websites?",
            "choices": [
                "ARPANET",
                "NSFNET",
                "Ethernet",
                "World Wide Web"
            ],
            "answer": "World Wide Web"
        }
    ]
}

    # Display the passage
    st.write("Read the following passage:")
    st.write(result_passage)

    # Initialize score
    score = 0

    # Display and check answers
    for question_data in questions_answers["questions"]:
        question = question_data["question"]
        result_question = app.translator_function(question, "en", app.language_mapping[to_language]).text
        choices = question_data["choices"]
        result_choices = [app.translator_function(choice, "en", app.language_mapping[to_language]).text for choice in choices]
        answer = question_data["answer"]
        result_answer = app.translator_function(answer, "en", app.language_mapping[to_language]).text
        user_answer = st.radio(result_question, result_choices)
        if user_answer == result_answer:
            score += 1

    # Display the score
    st.write(f"Your score: {score}/{len(questions_answers['questions'])}")