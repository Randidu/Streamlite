import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Summarization Tool")

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer_model = load_model()

st.title("Text Summarization Tool")
col1, col2 = st.columns([2,1])
with col1:
    user_input =st.text_area("Enter text to summarize", height=200)
    summarizer_button = st.button("Summarize Text", type="primary")

with col2:
    st.markdown("Powered by C Clarke Institute Students")

if summarizer_button and user_input:
    with st.spinner("Summarizing......"):
        result = summarizer_model(user_input)
        summary_text = result[0]['summary_text']
        st.markdown(summary_text)

elif summarizer_button:
    st.warning("Please Enter some text to summarize")