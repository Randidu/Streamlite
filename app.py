import streamlit as st
from transformers import pipeline
from PIL import Image
st.set_page_config(page_title="AI Summarization Tool")

@st.cache_resource
def load_summarization_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_resource
def load_captioning_model():
    return pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")


captioning_model=load_captioning_model()
summarizer_model = load_summarization_model()

st.title("Image caption")
col1, col2 = st.columns([2,1])
with col1:
    # user_input =st.text_area("Enter text to summarize", height=200)
    uploaded_image= st.file_uploader("Upload an image ",type=["png","jpg","jpeg"])
    caption_generate = st.button("Generate caption", type="primary")

with col2:
    st.markdown("Powered by C Clarke Institute Students")

if uploaded_image and caption_generate:
    with st.spinner("Generate caption"):
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image)

        result = captioning_model(image)
        gen_text = result[0]['generated_text']
        st.markdown(gen_text)

elif caption_generate:
    st.warning("Please Enter some image")