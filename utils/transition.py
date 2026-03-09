import streamlit as st
import time

def page_transition(animation="fade"):
    animations = {
        "fade": """
            <style>
            .stApp {
                animation: fadeIn 0.6s ease-in-out;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            </style>
        """,

        "slide": """
            <style>
            .stApp {
                animation: slideIn 0.6s ease-in-out;
            }
            @keyframes slideIn {
                from { transform: translateX(50px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            </style>
        """
    }

    st.markdown(animations.get(animation, ""), unsafe_allow_html=True)
