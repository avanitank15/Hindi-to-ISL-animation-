import streamlit as st
from utils.style import load_css
from utils.transition import page_transition
import base64

# 1. Page Configuration
st.set_page_config(page_title="Home", layout="wide")

# 2. Load global CSS + transition
load_css()
page_transition("fade")

# 3. Load GIF as base64
def get_base64_gif(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

gif_base64 = get_base64_gif("assets/character.gif")

# ---------- STYLES ----------
st.markdown(
    f"""
    <style>

    .stApp {{
        background: #F4F4F4;
        min-height: 100vh;
        padding-bottom: 60px;
    }}

    /* ===== DISGUISED ABOUT BUTTON (No Box) ===== */
    /* Target tertiary button specifically to hide background/border */
    button[kind="tertiary"] {{
        background-color: transparent !important;
        color: #4f46e5 !important; 
        border: none !important;
        padding: 0 !important;
        font-size: 1rem !important;
        text-decoration: none !important;
        box-shadow: none !important;
        min-height: 0px !important;
        line-height: 1.5 !important;
        display: inline-flex !important;
        justify-content: flex-start !important;
    }}

    button[kind="tertiary"]:hover {{
        color: #ff7f50 !important;
        background-color: transparent !important;
        text-decoration: underline !important;
    }}

    button[kind="tertiary"]:active, button[kind="tertiary"]:focus {{
        background-color: transparent !important;
        outline: none !important;
        box-shadow: none !important;
    }}

    /* ===== Floating shapes ===== */
    .float-shape {{
        position: fixed;
        border-radius: 50%;
        opacity: 0.18;
        filter: blur(2px);
        animation: float 12s ease-in-out infinite;
        z-index: 0;
    }}

    .shape1 {{
        width: 220px; height: 220px;
        background: #ff7f50;
        top: 20%; left: 5%;
    }}

    .shape2 {{
        width: 200px; height: 200px;
        background: #ff6f61;
        bottom: 10%; right: 38%;
        animation-delay: 4s;
    }}

    @keyframes float {{
        0%   {{ transform: translateY(0px); }}
        50%  {{ transform: translateY(-30px); }}
        100% {{ transform: translateY(0px); }}
    }}

    /* ===== Character ===== */
    .character-fixed {{
        position: fixed;
        right: 2%;
        bottom: 80px;
        width: 400px;
        z-index: 100;
        pointer-events: none;
    }}

    .character-gif {{
        width: 400px;
        animation: character-float 4s ease-in-out infinite;
    }}

    @keyframes character-float {{
        0%, 100% {{ transform: translateY(0px); }}
        50%       {{ transform: translateY(-14px); }}
    }}

    /* ===== Title ===== */
    .product-title {{
        font-size: 2.8rem;
        font-weight: 800;
        color: #1e1b4b;
    }}

    /* ===== Bottom Bar ===== */
    .bottom-bar {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50px;
        background: linear-gradient(90deg, #FF8C94, #FFAAA6, #FFD3B5, #FFAAA6, #FF8C94);
        background-size: 200% 100%;
        animation: gradientShift 8s ease infinite;
        color: #2d3748;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999999;
        border-top: 3px solid #FF8C94;
        box-shadow: 0 -4px 20px rgba(255, 140, 148, 0.3);
        overflow: hidden;
    }}

    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .bottom-bar span {{
        white-space: nowrap;
        animation: moveText 15s linear infinite;
    }}

    @keyframes moveText {{
        from {{ transform: translateX(100%); }}
        to   {{ transform: translateX(-100%); }}
    }}

    /* ===== Description ===== */
    .product-description {{
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        max-width: 520px;
        font-size: 1.05rem;
        line-height: 1.7;
        background: rgba(255,255,255,0.6);
        border-left: 4px solid #4f46e5;
        border-radius: 8px;
        padding: 1rem;
        color: #374151;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------- FLOATING SHAPES ----------
st.markdown('<div class="float-shape shape1"></div>', unsafe_allow_html=True)
st.markdown('<div class="float-shape shape2"></div>', unsafe_allow_html=True)

# ---------- CHARACTER ----------
st.markdown(
    f"""
    <div class="character-fixed">
        <img class="character-gif"
             src="data:image/gif;base64,{gif_base64}">
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CONTENT ----------
st.markdown('<div class="product-title">Hindi to ISL Machine</div>', unsafe_allow_html=True)

st.markdown("""
<div class="product-description">
    Bridging the gap between spoken Hindi and Indian Sign Language (ISL) —
    making communication seamless, inclusive, and accessible.
</div>
""", unsafe_allow_html=True)

# Disguised About Link
if st.button("↗ Click to learn more", type="tertiary"):
    st.switch_page("pages/about.py")

# THE DIVIDER (Added back)
st.markdown("---")

# ---------- ACTION BUTTONS ----------
col1, col2, col3 = st.columns([2, 3, 5])

with col1:
    # In home.py — change this line:
    if st.button("Login"):
        st.switch_page("pages/login.py")   # was pages/form.py

with col3:
    if st.button("Translate Hindi to ISL", type="primary"):
        st.switch_page("pages/main.py")

# ---------- BOTTOM BAR ----------
st.markdown("""
<div class="bottom-bar">
    <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
</div>
""", unsafe_allow_html=True)