import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
        /* ===== GLOBAL APP STYLES ===== */
        :root {
            --bottombar-height: 52px;
        }

        .stApp {
            background-color: #eef1f8;
            padding-bottom: var(--bottombar-height); /* Prevent overlap */
        }

        /* Headings */
        h1 { color: #1f2937; font-weight: 700; font-size: 3rem; }
        h3 { color: #2563eb; font-size: 1.8rem; }

        label {
            color: #4f46e5 !important;
            font-weight: 500;
            font-size: 1.2rem;
        }

        /* ===== BOTTOM BAR STYLES ===== */
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
            text-align: center;
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

        /* ===== FLOATING BACKGROUND SHAPES ===== */
        .float-shape {
            position: fixed;
            border-radius: 50%;
            opacity: 0.1;
            filter: blur(60px);
            animation: float 12s ease-in-out infinite;
            z-index: -1;
        }
        .shape1 { width: 300px; height: 300px; background: #2563eb; top: 20%; left: 5%; }
        .shape2 { width: 350px; height: 350px; background: #4f46e5; bottom: 10%; right: 5%; animation-delay: 4s; }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%      { transform: translateY(-20px); }
        }

        /* ===== UNIVERSAL BUTTON STYLE ===== */
        button {
            background: linear-gradient(135deg, #2563eb, #4f46e5) !important;
            color: white !important;
            font-size: 20px !important;
            font-weight: 600 !important;
            padding: 14px 30px !important;
            border-radius: 14px !important;
            border: none !important;
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.35);
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            width: 100%;
        }

        button:hover {
            transform: translateY(-3px) scale(1.03) !important;
            box-shadow: 0 10px 28px rgba(79, 70, 229, 0.45) !important;
            filter: brightness(1.08);
        }

        /* Textareas and Cards */
        .card {
            background-color: #ffffff;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        }

        textarea {
            background-color: #f9fafb !important;
            color: #6d28d9 !important;
            font-size: 20px !important;
            border-radius: 12px !important;
        }
        </style>

        <div class="top-bar">
            <span>✨ Welcome • Hindi to ISL Translator • Inclusive Communication • Accessibility First ✨</span>
        </div>
        <div class="float-shape shape1"></div>
        <div class="float-shape shape2"></div>
        """,
        unsafe_allow_html=True
    )