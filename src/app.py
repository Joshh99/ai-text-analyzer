import streamlit as st
from utils.text_analyzer import TextAnalyzer
import pickle

# Instantiate the TextAnalyzer class
text_analyzer = TextAnalyzer(model_name="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

st.set_page_config(
    page_title="Text Analyzer App", 
    layout="wide", 
    page_icon="📝"
    )

# with st.spinner("Loading model..."):
#     text_analyzer = TextAnalyzer(model_name="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
#     st.success("Model loaded successfully!")

with st.container():
    st.title("Text Analyzer App")
    st.markdown("---")
    st.header("Sentiment Analysis")
    st.write("Enter a text to analyze its sentiment:")
    text_input = st.text_area("Text:")
    if st.button("Analyze"):
        if text_input:
            with st.spinner("Analyzing..."):
                result = text_analyzer.sentiment_analysis([text_input])
                st.subheader("Analysis Result:")
                st.write(result[0]['label'])
        else:
            st.warning("Please enter a text to analyze!")

with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)
