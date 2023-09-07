import streamlit as st
from streamlit_tags import st_tags
from prompt_generator import generate_prompt
from PIL import Image

favicon = Image.open("favicon.ico")
st.set_page_config(page_title="Image Prompt Generator", page_icon=favicon)

st.title("Image Prompt Generator")
st.markdown("##")

input_form = st.form("forms")
output_container = st.container()

def display_prompt() :
    with st.spinner('Generating...'):
        prompts = generate_prompt(nprompt, style, keywords)
        if len(prompts) != nprompt  :
            display_prompt() 
        for i,prompt in enumerate(prompts):
            output_container.divider()
            output_container.markdown(f"### Prompt {i+1} :")
            output_container.markdown(f"##### *{prompt}*")

with input_form:
    keywords = st_tags(
        label='#### Enter Keywords ...',
        text='Press enter to add more (max 5 keywords)',
        maxtags=5)

    c1, c2 = st.columns(2)
    nprompt = c1.select_slider("Select Number of Prompts ...", options=[1, 2, 3, 4, 5])
    style = c2.selectbox("Select Art Style ...", options=["Realistic", "Anime", "Watercolor", "Academicism painting", "John Collier", "Salvador Dali", "Android Jones"])

    if st.form_submit_button("Generate Prompt"):
        if keywords :
            display_prompt()
        else :
            st.warning("Pleae select keywords ...")