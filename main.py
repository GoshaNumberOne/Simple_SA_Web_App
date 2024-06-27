from textblob import TextBlob
from dataclasses import dataclass
import streamlit as st

@dataclass
class Mood:
    polarity: str
    sentiment: float

@dataclass
class Subjectivity:
    essence: str
    value: float

def get_mood(input_text: str, *, threshold: float) -> Mood:

    sentiment: float = round(TextBlob(input_text).sentiment.polarity, 2)

    positive_threshold: float = threshold
    negative_threshold: float = -threshold

    if sentiment >= positive_threshold:
        return Mood("Positive", sentiment)
    elif sentiment <= negative_threshold:
        return Mood("Negative", sentiment)
    else:
        return Mood("Neutral", sentiment)

def get_subjectivity(input_text: str):

    subjectivity: float = round(TextBlob(input_text).sentiment.subjectivity, 2)

    if subjectivity == 1:
        return Subjectivity("Subjectively", subjectivity)
    elif subjectivity == 0:
        return Subjectivity("Objectively", subjectivity)
    elif 0 < subjectivity < 0.5:
        return Subjectivity("Quite objectively", subjectivity)
    elif 0.5 < subjectivity < 1:
        return Subjectivity("Quite subjectively", subjectivity)



st.header('Sentiment Analysis')

with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        mood: Mood = get_mood(text, threshold=0.3)
        sudj: Subjectivity = get_subjectivity(text)

        st.write('Polarity: ', f'{mood.polarity} ({mood.sentiment})')
        st.write('Subjectivity: ', f'{sudj.essence} ({sudj.value})')



