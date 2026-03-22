# import streamlit as st
# from utils.style import load_css
# from utils.transition import page_transition

# page_transition("fade")
# load_css() 

# st.title("Home")
# st.write("welcome to ____")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button(" Login "):
#         st.switch_page("pages/form.py")

# with col2:
#     if st.button("Translate Hindi to ISL"):
#         st.switch_page("pages/main.py")
import streamlit as st
from utils.style import load_css
from utils.transition import page_transition

# 1. Page Configuration
st.set_page_config(page_title="Home", layout="wide")

# 2. Load your original global CSS
load_css()
page_transition("fade")

# 3. HOME PAGE SPECIFIC OVERRIDES
st.markdown(
    """
    <style>
    :root {
        --bottombar-height: 56px;
    }

    /* Prevent overlap with fixed bottom bar */
    .stApp {
        padding-bottom: var(--bottombar-height);
    }

    /* ===== Bottom moving bar (Blue Theme) ===== */
    .top-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: var(--bottombar-height);
        background: linear-gradient(90deg, #2563eb, #4f46e5, #2563eb);
        color: white !important;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
        overflow: hidden;
    }

    .top-bar span {
        display: inline-block;
        white-space: nowrap;
        animation: moveText 15s linear infinite;
        font-size: 1.1rem;
    }

    @keyframes moveText {
        from { transform: translateX(100%); }
        to   { transform: translateX(-100%); }
    }

    /* ===== Floating background shapes ===== */
    .float-shape {
        position: fixed;
        border-radius: 50%;
        opacity: 0.18;
        filter: blur(2px);
        animation: float 12s ease-in-out infinite;
        z-index: 0;
    }

    .shape1 {
        width: 220px;
        height: 220px;
        background: #c084fc;
        top: 20%;
        left: 5%;
    }

    .shape2 {
        width: 300px;
        height: 300px;
        background: #a78bfa;
        bottom: 10%;
        right: 8%;
        animation-delay: 4s;
    }

    @keyframes float {
        0%   { transform: translateY(0px); }
        50%  { transform: translateY(-30px); }
        100% { transform: translateY(0px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- BOTTOM BAR ----------
st.markdown(
    """
    <div class="top-bar">
        <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- FLOATING SHAPES ----------
st.markdown(
    """
    <div class="float-shape shape1"></div>
    <div class="float-shape shape2"></div>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENT ----------
st.title("Home")
st.write("Welcome to the Hindi-ISL Bridge")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("Login"):
        st.switch_page("pages/form.py")

with col2:
    if st.button("Translate Hindi to ISL"):
        st.switch_page("pages/main.py")