import streamlit as st
from pathlib import Path
import base64

def get_gif_base64(gif_path: str) -> str:
    with open(gif_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def show():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Ensure entire background is #F4F4F4 */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #F4F4F4 !important;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F4F4F4;
    }

    .main { background-color: #F4F4F4; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }

    .page-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #111;
        margin-bottom: 4px;
    }
    .page-subtitle {
        font-size: 1rem;
        color: #666;
        font-weight: 400;
        margin-bottom: 24px;
    }

    .divider {
        border: none;
        border-top: 1px solid #ddd;
        margin: 28px 0;
    }

    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #111;
        margin-bottom: 10px;
    }

    .body-text {
        font-size: 0.95rem;
        color: #444;
        line-height: 1.8;
    }

    .stat-row {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        margin: 20px 0;
    }
    .stat-box {
        background: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 16px 22px;
        min-width: 130px;
        text-align: center;
    }
    .stat-num {
        font-size: 1.6rem;
        font-weight: 700;
        color: #111;
    }
    .stat-lbl {
        font-size: 0.75rem;
        color: #888;
        margin-top: 2px;
    }

    .feat-row {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 14px;
        margin: 16px 0;
    }
    .feat-item {
        background: #fff;
        border: 1px solid #e8e8e8;
        border-radius: 10px;
        padding: 18px 16px;
    }
    .feat-name { font-size: 0.88rem; font-weight: 600; color: #222; margin-bottom: 4px; }
    .feat-desc { font-size: 0.8rem; color: #777; line-height: 1.5; }

    .pipeline-row {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 6px;
        margin: 16px 0;
    }
    .pipe-box {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px 14px;
        font-size: 0.8rem;
        font-weight: 500;
        color: #333;
        text-align: center;
    }
    .pipe-sep { color: #bbb; font-size: 1rem; }

    .tag-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }
    .tag {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 6px 12px;
        font-size: 0.8rem;
        color: #555;
    }

    .gif-section {
        text-align: right;
        margin-bottom: 8px;
    }
    .gif-caption {
        font-size: 0.85rem;
        color: #888;
        margin-top: 10px;
        font-style: italic;
    }

    .footer-note {
        text-align: center;
        font-size: 0.82rem;
        color: #aaa;
        margin-top: 32px;
        padding-top: 20px;
        border-top: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

    # Top Section: Title & Mission (Left) and GIF (Right)
    col1, col2 = st.columns([2.5, 1])

    with col1:
        st.markdown('<div class="page-title">About This Project</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Text & Speech -> Indian Sign Language | Multilingual | Animated</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-title">Our Mission</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="body-text">
            India has over <strong>63 million</strong> Deaf and Hard of Hearing (DHH) individuals, yet only
            <strong>1–2% of deaf children</strong> have access to formal Indian Sign Language education.
            Nearly <strong>99% drop out of school before age 12</strong> due to a shortage of ISL resources
            and trained instructors.<br><br>
            This system converts text and speech from multiple Indian languages into animated ISL,
            making communication and education more accessible — no special hardware needed.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # GIF Section at the Top Right
        gif_path = Path(__file__).parent.parent / "assets" / "we-love-our-community.gif"
        
        try:
            gif_b64 = get_gif_base64(str(gif_path))
            st.markdown(f"""
            <div class="gif-section">
                <img src="data:image/gif;base64,{gif_b64}" width="100%" style="max-width:220px; border-radius:12px;" />
            </div>
            """, unsafe_allow_html=True)
        except FileNotFoundError:
            st.markdown(f"""
            <div class="gif-section">
                <div style="font-size:1rem; color:#888; border:1px dashed #ccc; padding:20px; text-align:center;">
                    We love our community<br><br><small>(Looking for GIF at: {gif_path})</small>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Stats 
    st.markdown("""
    <div class="stat-row">
        <div class="stat-box"><div class="stat-num">63M+</div><div class="stat-lbl">DHH individuals in India</div></div>
        <div class="stat-box"><div class="stat-num">2</div><div class="stat-lbl">Supported languages</div></div>
        <div class="stat-box"><div class="stat-num">400+</div><div class="stat-lbl">ISL data samples</div></div>
        <div class="stat-box"><div class="stat-num">2D</div><div class="stat-lbl">Animated ISL avatar</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Features 
    st.markdown('<div class="section-title">What It Does</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="feat-row">
        <div class="feat-item"><div class="feat-name">Multilingual Input</div><div class="feat-desc">Supports both Hindi and English</div></div>
        <div class="feat-item"><div class="feat-name">ISL Gloss</div><div class="feat-desc">Converts text into ISL grammar following sign language rules.</div></div>
        <div class="feat-item"><div class="feat-name">2D Avatar</div><div class="feat-desc">Animated ISL notation in real time.</div></div>
        <div class="feat-item"><div class="feat-name">Speech Input</div><div class="feat-desc">Supports audio transcription for speech-to-ISL flow.</div></div>
        <div class="feat-item"><div class="feat-name">ISL Dictionary</div><div class="feat-desc"></div></div>
        <div class="feat-item"><div class="feat-name">Education-Ready</div><div class="feat-desc">Built for schools, hospitals & government portals.</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Pipeline 
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="pipeline-row">
        <div class="pipe-box">Text / Audio</div><span class="pipe-sep">-></span>
        <div class="pipe-box">NLP Cleaning</div><span class="pipe-sep">-></span>
        <div class="pipe-box">Multilingual Translation</div><span class="pipe-sep">-></span>
        <div class="pipe-box">ISL Gloss</div><span class="pipe-sep">-></span>
        <div class="pipe-box">Animated Dataset</div><span class="pipe-sep">-></span>
        <div class="pipe-box">2D Avatar</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # # Tech Stack 
    # st.markdown('<div class="section-title">Tech Stack</div>', unsafe_allow_html=True)
    # st.markdown("""
    # <div class="tag-row">
    #     <span class="tag">Streamlit</span>
    #     <span class="tag">Python</span>
    #     <span class="tag">spaCy | NLTK</span>
    #     <span class="tag">M2M100 | CTranslate2</span>
    #     <span class="tag">Qwen-asr</span>
    #     <span class="tag">iSign Dataset</span>
    # </div>
    # """, unsafe_allow_html=True)

    # Footer 
    st.markdown("""
    <div class="footer-note">
         Non-commercial research use only
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="About - ISL Translator",
        layout="wide"
    )
    show()