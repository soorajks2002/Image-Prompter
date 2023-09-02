import streamlit as st
from streamlit_tags import st_tags
from prompt_generator import generate_prompt
from PIL import Image

favicon = Image.open("favicon.ico")
st.set_page_config(page_title="Image Prompt Generator", page_icon=favicon)

st.title("Image Prompt Generator")
st.markdown("##")

with st.form("forms") :

    keywords = st_tags(
        label='#### Enter Keywords:',
        text='Press enter to add more (max 5 keywords)',
        maxtags=5)

    if st.form_submit_button("Generate Prompt") and keywords :
        with st.spinner('Generating...'):
            for i in range(2) :
                st.divider()
                prompt = generate_prompt(keywords)
                st.markdown(f"## Prompt {i+1} :")
                st.markdown(f"#### *{prompt}*")