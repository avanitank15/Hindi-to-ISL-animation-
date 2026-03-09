
# import streamlit as st
# from time import sleep


# st.set_page_config(
#     page_title="My Streamlit App",
#     page_icon="🏠",
#     layout="centered"
# )
# st.title("Welcome to My Website")
# st.write("Use the sidebar to navigate.")


import streamlit as st
import time

# from utils.style import load_css
# from utils.transition import page_transition

# page_transition("fade")
# load_css() 

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🏠",
    layout="centered"
)
from utils.style import load_css
from utils.transition import page_transition

page_transition("fade")
load_css() 


st.title("Welcome to My Website")
st.write("Preparing your experience...")

st.markdown(
    """
    <style>
    .stSpinner {
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Smooth transition effect
with st.spinner("Loading Home Page..."):
    time.sleep(1.5)  # controls smoothness

st.switch_page("pages/home.py")
