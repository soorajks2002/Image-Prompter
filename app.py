import streamlit as st
from streamlit_tags import st_tags
from prompt_generator import generate_prompt

st.set_page_config(page_title="Image Prompt Generator")

st.title("Image Prompt Generator")

keywords = st_tags(
    label='#### Enter Keywords:',
    text='Press enter to add more',
    maxtags=5)

if st.button("SUBMIT") and keywords :
    with st.spinner('Generating...'):
        prompt = generate_prompt(keywords)
    st.header("Prompt :")
    st.markdown(f"#### {prompt}")