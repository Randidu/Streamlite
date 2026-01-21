import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Summarization Tool")

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer_model = load_model()

st.title("Text Summarizer Tool")
col1, col2 = st.columns([1, 2])

with col1:
    user_input = st.text_area("Enter text to summarize", height=200)
    summarizer_button = st.button("Summarize Text", type="primary")

with col2:
    st.markdown("Powered by C Clarke Institute Student")

if summarizer_button:
    if user_input.strip():
        with st.spinner("Summarizing..."):
            result = summarizer_model(user_input)
            summary_text = result[0]['summary_text']
            st.markdown("### Summary:")
            st.markdown(summary_text)
    else:
        st.warning("Please enter some text to summarize...")