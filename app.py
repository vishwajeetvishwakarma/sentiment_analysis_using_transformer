import streamlit as st
import pandas as pd
import transformers


model = transformers.pipeline("text-classification", model="model" , device=0)

def get_results(input_text):
    results = model(input_text)
    return int(results[0]['label'].split('_')[1])

heading = st.title("Sentiment Analysis")

input_text = st.text_area("Enter text to analyze")
if st.button("Analyze"):
    result = get_results(input_text)
    print(result)
    if result == 0:
        st.write("Negative😔")
    elif result == 1:
        st.write("Neutral😐")
    else:
        st.write("Positive😀")