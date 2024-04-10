import app
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator
translator = Translator()

def page_3():
        isTranslateOn = False
        def main_process(output_placeholder, from_language, to_language):      
            while isTranslateOn:
                rec = sr.Recognizer()
                with sr.Microphone() as source:
                    output_placeholder.text("Listening...")
                    rec.pause_threshold = 1
                    audio = rec.listen(source, phrase_time_limit=10)
                try:
                    output_placeholder.text("Processing...")
                    spoken_text = rec.recognize_google(audio, language='{}'.format(from_language))
                    output_placeholder.text("Translating...")
                    translated_text = app.translator_function(spoken_text, from_language, to_language)
                    app.text_to_voice(translated_text.text, to_language)
                    # Force the UI to update immediately
                    st.experimental_rerun()
                except Exception as e:
                    print(e)
        st.title("Translate your voice into multiple languages")
        # Dropdowns for selecting languages
        from_language_name = st.selectbox("Select Source Language:", list(LANGUAGES.values()), key="from_language")
        to_language_name = st.selectbox("Select Target Language:", list(LANGUAGES.values()), key="to_language")
        # Convert language names to language codes
        from_language = app.get_language_code(from_language_name)
        to_language = app.get_language_code(to_language_name)
        # Button to trigger translation
        start_button = st.button("Start")
        stop_button = st.button("Stop")
        # Check if "Start" button is clicked
        if start_button:
            if not isTranslateOn:
                isTranslateOn = True
                output_placeholder = st.empty()
                main_process(output_placeholder, from_language, to_language)
        # Check if "Stop" button is clicked
        if stop_button:
            isTranslateOn = False