import streamlit as st
from pathlib import Path
import base64

# Page Configuration

st.set_page_config(
    page_title="RoomSync AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
css_path = Path(__file__).parent / "assets" / "css" / "main.css"

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Background

image_path = Path(__file__).parent / "assets" / "images" / "background.jpg"

with open(image_path, "rb") as img:
    encoded = base64.b64encode(img.read()).decode()

st.markdown(
    f"""
<style>

.stApp{{
    background:
        linear-gradient(
            rgba(8,10,20,.58),
            rgba(8,10,20,.72)
        ),
        url("data:image/jpeg;base64,{encoded}");

    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}}

</style>
""",
    unsafe_allow_html=True,
)

# NOW render page

from pages.home import show_home

show_home()
