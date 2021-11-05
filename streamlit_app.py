from transformers import pipeline
import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.success('Gratulacje! Aplikacja gotowa do działania')

st.title('Emocjonalny translator')
st.image("SUML/logo.jpg")

st.header('O aplikacji')

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')

st.write('Aplikacja pozwala na sprawdzenie wydzwięku emocjonalnego sentencji. Interesujacą frazę należy wpisać w języku angielskim. Ponadto można szybko i przyjemnie przetłumaczyć dowolną sentencję z języka angielskiego na niemiecki. W tym celu należy wybrać odpowiednią fuznkcję z rozwijanej listy.')

st.header('Przetwarzanie języka naturalnego')


option = st.selectbox(
    "Opcje",
    [
        "Translator eng - de",
        "Wydźwięk emocjonalny tekstu (eng)"
    ]
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text="Próbuję zweryfikować jakie emocje towarzyszą temu co napisłeś..."):
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
        st.success("Już wiem...")
        st.balloons()
        st.write(answer)

if option == "Translator eng - de":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text="Jestem w trakcie tłumaczenia. Cierpliwości niemiecki to trudny język..."):
            action = pipeline("translation_en_to_de")
            gerText = action(text, max_length=40)
        st.success("No i mamy to...")
        st.balloons()
        st.write(gerText)


st.subheader('Autor: s18325')
