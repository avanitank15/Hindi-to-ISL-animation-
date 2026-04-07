# import streamlit as st

# from utils.style import load_css
# from utils.transition import page_transition

# page_transition("fade")
# load_css()

# st.title("user login form")

# form_values= {
#     "name": None,
#     "age": None,
#     "gender": None,
#     "ISLSpeaker": None
# }
# with st.form(key="userInfoForm"):
#     form_values["name"]=st.text_input("enter yopur name")
#     form_values["age"]=st.number_input("enter your age",step=1)
#     form_values["gender"]=st.radio("Gender",["male","Female"])
#     form_values["ISLSpeaker"]=st.radio("have you learned ISL",["YES","NO"])
#     # form_values["Languages"]=st.checkbox
    
#     submit_button=st.form_submit_button("Login")
#     if submit_button:
#         if not all(form_values.values()):
#             st.warning("please fill all the fields")
#         else:
#             st.balloons()
#             st.write("### please confirm your Information")
#             for (key, value) in form_values.items():
#                 st.write(f"{key}:{value}")
    
# import streamlit as st
# import re
# import datetime

# # ─── Page config ────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="User Registration",
#     page_icon="👤",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ─── Custom CSS ─────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# /* ── Palette — matches the site's CSS variables ── */
# :root {
#     --bottombar-height: 52px;
#     --mint:   #A8E6CE;
#     --sage:   #DCEDC2;
#     --peach:  #FFD3B5;
#     --coral:  #FFAAA6;
#     --salmon: #FF8C94;

#     --text:      #2d3748;
#     --text-soft: #e85d6c;
#     --success:   #5cb88a;
#     --error:     #e85d6c;
#     --warn:      #f59e0b;
#     --white:     #ffffff;
#     --off-white: #fefefe;
# }

# /* ── Global ── */
# html, body, [data-testid="stAppViewContainer"] {
#     background: linear-gradient(135deg, var(--sage) 0%, var(--peach) 100%) !important;
#     font-family: 'Segoe UI', sans-serif;
#     color: var(--text);
#     padding-bottom: var(--bottombar-height);
# }
# [data-testid="stHeader"]  { background: transparent !important; }
# [data-testid="stToolbar"] { display: none; }
# .block-container { padding: 2rem 3rem !important; max-width: 1100px !important; }

# /* ── Floating background shapes (matches site) ── */
# .float-shape {
#     position: fixed;
#     opacity: 0.22;
#     filter: blur(80px);
#     animation: floatAnim 12s ease-in-out infinite;
#     z-index: -1;
#     pointer-events: none;
# }
# .shape1 { width:280px; height:280px; background:var(--mint);   top:12%;    left:2%;   border-radius:4px; transform:rotate(15deg); }
# .shape2 { width:320px; height:320px; background:var(--salmon); bottom:12%; right:2%;  border-radius:4px; transform:rotate(-10deg); animation-delay:4s; }
# .shape3 { width:200px; height:200px; background:var(--coral);  top:50%;    right:14%; border-radius:4px; transform:rotate(25deg);  animation-delay:2s; }
# @keyframes floatAnim {
#     0%,100% { transform: translateY(0px)   rotate(15deg); }
#     50%      { transform: translateY(-22px) rotate(15deg); }
# }

# /* ── Hero banner ── */
# .hero {
#     background: var(--white);
#     border: 2px solid var(--mint);
#     border-radius: 4px;
#     box-shadow: 6px 6px 0px #8ed4b8;
#     padding: 2.2rem 2.8rem;
#     margin-bottom: 2rem;
#     position: relative;
#     overflow: hidden;
# }
# .hero::after {
#     content: '';
#     position: absolute;
#     top: -40px; right: -40px;
#     width: 180px; height: 180px;
#     background: var(--sage);
#     border-radius: 4px;
#     opacity: .4;
#     transform: rotate(20deg);
# }
# .hero-title {
#     font-size: 2.6rem;
#     font-weight: 800;
#     color: var(--text);
#     letter-spacing: -0.5px;
#     margin: 0 0 .3rem;
# }
# .hero-title span { color: var(--salmon); }
# .hero-sub { color: #718096; font-size: .95rem; margin: 0; }

# /* ── Section labels ── */
# .section-label {
#     font-size: .7rem;
#     font-weight: 800;
#     letter-spacing: .2em;
#     text-transform: uppercase;
#     color: var(--salmon);
#     margin: 1.8rem 0 .7rem;
#     display: flex;
#     align-items: center;
#     gap: .6rem;
# }
# .section-label::after {
#     content: '';
#     flex: 1;
#     height: 2px;
#     background: var(--coral);
#     opacity: .4;
# }

# /* ── Streamlit input overrides ── */
# [data-testid="stTextInput"] > div > div,
# [data-testid="stNumberInput"] > div > div,
# [data-testid="stDateInput"] > div > div {
#     background: var(--off-white) !important;
#     border: 2px solid var(--sage) !important;
#     border-radius: 4px !important;
#     transition: border-color .2s, box-shadow .2s;
# }
# [data-testid="stTextInput"] > div > div:focus-within,
# [data-testid="stNumberInput"] > div > div:focus-within,
# [data-testid="stDateInput"] > div > div:focus-within {
#     border-color: var(--mint) !important;
#     box-shadow: 0 0 0 3px rgba(168,230,206,.35) !important;
# }
# [data-testid="stTextInput"] input,
# [data-testid="stNumberInput"] input,
# [data-testid="stDateInput"] input {
#     color: var(--text) !important;
#     font-size: 15px !important;
# }

# /* Labels */
# label[data-testid="stWidgetLabel"] p {
#     color: var(--text) !important;
#     font-size: .92rem !important;
#     font-weight: 600 !important;
# }

# /* Radio — clean native look, just accent the dot */
# [data-testid="stRadio"] > div {
#     gap: .2rem !important;
#     flex-wrap: wrap;
# }
# [data-testid="stRadio"] label {
#     background: transparent !important;
#     border: none !important;
#     border-radius: 0 !important;
#     padding: .2rem .4rem !important;
#     box-shadow: none !important;
#     font-size: .92rem !important;
#     font-weight: 500 !important;
#     color: var(--text) !important;
#     cursor: pointer;
#     transition: color .15s;
# }
# [data-testid="stRadio"] label:hover {
#     color: var(--salmon) !important;
#     transform: none !important;
# }
# [data-testid="stRadio"] label:has(input:checked) {
#     background: transparent !important;
#     border: none !important;
#     color: var(--salmon) !important;
#     font-weight: 700 !important;
#     box-shadow: none !important;
#     transform: none !important;
# }
# /* Show the actual radio dot, styled with salmon accent */
# [data-testid="stRadio"] input {
#     display: inline-block !important;
#     accent-color: var(--salmon) !important;
#     width: 15px !important;
#     height: 15px !important;
#     margin-right: 4px !important;
#     cursor: pointer;
# }

# /* Selectbox */
# [data-testid="stSelectbox"] > div > div {
#     background: var(--off-white) !important;
#     border: 2px solid var(--sage) !important;
#     border-radius: 4px !important;
#     color: var(--text) !important;
# }

# /* Slider */
# [data-testid="stSlider"] [role="slider"] {
#     background: var(--salmon) !important;
#     border-color: var(--salmon) !important;
# }

# /* Checkbox */
# [data-testid="stCheckbox"] label {
#     font-weight: 600 !important;
#     color: var(--text) !important;
#     font-size: .9rem !important;
# }

# /* Textarea */
# textarea {
#     background: var(--off-white) !important;
#     color: var(--text) !important;
#     font-size: 15px !important;
#     border-radius: 4px !important;
#     border: 2px solid var(--sage) !important;
#     transition: border-color .2s, box-shadow .2s;
# }
# textarea:focus {
#     border-color: var(--mint) !important;
#     box-shadow: 0 0 0 3px rgba(168,230,206,.35) !important;
# }

# /* Submit button — matches site universal button */
# [data-testid="stFormSubmitButton"] button {
#     background: linear-gradient(135deg, var(--salmon), var(--coral)) !important;
#     color: var(--text) !important;
#     font-size: 17px !important;
#     font-weight: 800 !important;
#     padding: 14px 28px !important;
#     border-radius: 4px !important;
#     border: 2px solid var(--salmon) !important;
#     box-shadow: 4px 4px 0px #e07a82 !important;
#     transition: all .15s ease !important;
#     width: 100% !important;
#     text-transform: uppercase !important;
#     letter-spacing: 1px !important;
#     margin-top: 1rem !important;
# }
# [data-testid="stFormSubmitButton"] button:hover {
#     transform: translate(-2px,-2px) !important;
#     box-shadow: 6px 6px 0px #e07a82 !important;
#     background: linear-gradient(135deg, var(--coral), var(--peach)) !important;
# }
# [data-testid="stFormSubmitButton"] button:active {
#     transform: translate(2px,2px) !important;
#     box-shadow: 2px 2px 0px #e07a82 !important;
# }

# /* Alerts */
# [data-testid="stAlert"] {
#     border-radius: 4px !important;
#     border-left-width: 4px !important;
#     font-weight: 600 !important;
# }

# /* Progress bar */
# .prog-wrap  { margin: .5rem 0 1.2rem; }
# .prog-label { font-size: .78rem; color: #718096; font-weight: 700; margin-bottom: .35rem; }
# .prog-bar-bg {
#     background: rgba(0,0,0,.08);
#     border-radius: 4px;
#     height: 8px;
#     overflow: hidden;
#     border: 1px solid rgba(0,0,0,.06);
# }
# .prog-bar-fill {
#     height: 100%;
#     border-radius: 4px;
#     transition: width .4s ease, background .4s;
# }

# /* Confirmation card — matches .card from site */
# .confirm-card {
#     background: var(--white);
#     border: 2px solid var(--mint);
#     border-radius: 4px;
#     box-shadow: 6px 6px 0px #8ed4b8;
#     padding: 1.6rem 2rem;
#     margin-top: 1.2rem;
# }
# .confirm-row {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     padding: .5rem 0;
#     border-bottom: 1px solid var(--sage);
#     font-size: .9rem;
# }
# .confirm-row:last-child { border-bottom: none; }
# .confirm-key { color: var(--text-soft); font-weight: 700; }
# .confirm-val { color: var(--text);      font-weight: 600; }

# /* Char counter */
# .char-count { font-size: .72rem; color: #718096; text-align: right; margin-top: .15rem; font-weight: 600; }
# .char-ok    { color: var(--success); }
# .char-bad   { color: var(--error); }

# /* Divider */
# hr.styled { border: none; border-top: 2px solid var(--sage); margin: 1.4rem 0; opacity: .7; }

# /* Scrollbar — matches site */
# ::-webkit-scrollbar       { width: 10px; }
# ::-webkit-scrollbar-track { background: var(--sage); }
# ::-webkit-scrollbar-thumb { background: var(--coral); border-radius: 2px; }
# ::-webkit-scrollbar-thumb:hover { background: var(--salmon); }
# ::selection { background: var(--mint); color: var(--text); }
# </style>

# <div class="float-shape shape1"></div>
# <div class="float-shape shape2"></div>
# <div class="float-shape shape3"></div>
# """, unsafe_allow_html=True)

# # ─── Validators ─────────────────────────────────────────────────────────────
# def is_valid_email(email: str) -> bool:
#     return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$", email))

# def is_valid_phone(phone: str) -> bool:
#     return bool(re.match(r"^\d{10}$", phone))

# def is_valid_name(name: str) -> bool:
#     return bool(name) and len(name.strip()) >= 2

# def completion_score(fv: dict) -> int:
#     fields = ["name", "dob", "gender", "phone", "email", "language", "ISLSpeaker"]
#     filled = sum(1 for f in fields if fv.get(f) not in [None, "", 0])
#     return int(filled / len(fields) * 100)

# def progress_html(pct: int) -> str:
#     if pct < 40:
#         colour = "#e85d6c"
#         label  = "Just getting started…"
#     elif pct < 75:
#         colour = "#f59e0b"
#         label  = f"{pct}% — Keep going!"
#     else:
#         colour = "#5cb88a"
#         label  = f"{pct}% — Almost there!" if pct < 100 else "✅ 100% — Ready to submit!"
#     return f"""
#     <div class="prog-wrap">
#         <div class="prog-label">Form completion · {label}</div>
#         <div class="prog-bar-bg">
#             <div class="prog-bar-fill" style="width:{pct}%; background:{colour};"></div>
#         </div>
#     </div>"""

# # ─── Hero ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <p class="hero-title">User <span>Registration</span></p>
#     <p class="hero-sub">Fill in your details below to create your ISL Translator profile.</p>
# </div>
# """, unsafe_allow_html=True)

# # ─── Session state ───────────────────────────────────────────────────────────
# for k in ("name_val", "phone_val", "email_val", "bio_val"):
#     if k not in st.session_state:
#         st.session_state[k] = ""

# # ─── Form ────────────────────────────────────────────────────────────────────
# with st.form(key="userInfoForm", clear_on_submit=False):

#     # ── Personal Info ──
#     st.markdown('<div class="section-label">👤 Personal Information</div>', unsafe_allow_html=True)

#     col1, col2 = st.columns(2, gap="large")
#     with col1:
#         name = st.text_input("Full Name *", value=st.session_state.name_val,
#                              placeholder="e.g. Ayushi Sharma", max_chars=60, key="_name_val")
#         name_ok  = is_valid_name(name)
#         name_cls = "char-ok" if name_ok else ("char-bad" if name else "")
#         st.markdown(f'<div class="char-count {name_cls}">{len(name)}/60 chars'
#                     + (' ✓' if name_ok else '') + '</div>', unsafe_allow_html=True)

#     with col2:
#         gender = st.radio("Gender *", ["Male", "Female", "Prefer not to say"],
#                           horizontal=True)

#     # Date of Birth — Native Calendar Input
#     dob = st.date_input(
#         "Date of Birth *",
#         value=None, 
#         min_value=datetime.date(1900, 1, 1),
#         max_value=datetime.date.today(),
#         format="DD/MM/YYYY"
#     )

#     # ── Contact ──
#     st.markdown('<div class="section-label">📬 Contact Details</div>', unsafe_allow_html=True)

#     col5, col6 = st.columns(2, gap="large")
#     with col5:
#         phone = st.text_input("Phone Number * (10 digits)", value=st.session_state.phone_val,
#                               placeholder="9876543210", max_chars=10, key="_phone_val")
#         phone_ok = is_valid_phone(phone)
#         ph_cls   = "char-ok" if phone_ok else ("char-bad" if phone else "")
#         st.markdown(f'<div class="char-count {ph_cls}">{len(phone)}/10 digits'
#                     + (' ✓' if phone_ok else '') + '</div>', unsafe_allow_html=True)

#     with col6:
#         email = st.text_input("Email Address *", value=st.session_state.email_val,
#                               placeholder="you@example.com", max_chars=80, key="_email_val")
#         email_ok = is_valid_email(email)
#         em_cls   = "char-ok" if email_ok else ("char-bad" if email else "")
#         st.markdown(f'<div class="char-count {em_cls}">'
#                     + ('Valid email ✓' if email_ok else (f'{len(email)}/80' if email else ''))
#                     + '</div>', unsafe_allow_html=True)

#     # ── Preferences & ISL ──
#     st.markdown('<div class="section-label">🌐 Preferences & ISL</div>', unsafe_allow_html=True)

#     col7, col8 = st.columns(2, gap="large")
#     with col7:
#         language = st.selectbox("Preferred Language *",
#                                 ["English", "Hindi", "Tamil", "Telugu",
#                                  "Kannada", "Bengali", "Marathi", "Gujarati"])
#         notification_pref = st.radio("Notification Preference",
#                                      ["Email", "SMS", "None"], horizontal=True)

#     with col8:
#         isl_speaker = st.radio("Have you learned ISL? *", ["Yes", "No"], horizontal=True)
#         if isl_speaker == "Yes":
#             isl_exp   = st.slider("Years of ISL Experience", 0, 40, 1,
#                                   help="Drag to set your years of experience")
#             isl_level = st.selectbox("Proficiency Level",
#                                      ["Beginner", "Elementary", "Intermediate", "Advanced", "Fluent"])
#         else:
#             isl_exp   = 0
#             isl_level = None

#     # ── Bio ──
#     st.markdown('<div class="section-label">📝 Short Bio (Optional)</div>', unsafe_allow_html=True)
#     bio = st.text_area("Tell us a little about yourself",
#                        value=st.session_state.bio_val,
#                        placeholder="I am a teacher who works with the deaf community…",
#                        max_chars=300, height=90, key="_bio_val")
#     bio_cls = "char-ok" if 10 <= len(bio) <= 300 else ("char-bad" if len(bio) > 300 else "")
#     st.markdown(f'<div class="char-count {bio_cls}">{len(bio)}/300</div>', unsafe_allow_html=True)

#     # ── Terms & progress ──
#     st.markdown("<hr class='styled'>", unsafe_allow_html=True)
#     agree = st.checkbox("I agree to the Terms & Conditions and Privacy Policy *")

#     score = completion_score({"name": name, "dob": dob, "gender": gender,
#                               "phone": phone, "email": email,
#                               "language": language, "ISLSpeaker": isl_speaker})
#     st.markdown(progress_html(score), unsafe_allow_html=True)

#     submitted = st.form_submit_button("🚀  Create Profile")

# # ─── Post-submit ─────────────────────────────────────────────────────────────
# if submitted:
#     errors = []
#     if not is_valid_name(name):   errors.append("Name must be at least 2 characters.")
#     if not dob:                   errors.append("Please provide your Date of Birth.")
#     if not is_valid_phone(phone): errors.append("Phone number must be exactly 10 digits.")
#     if not is_valid_email(email): errors.append("Please enter a valid email address.")
#     if not agree:                 errors.append("You must accept the Terms & Conditions.")

#     if errors:
#         for err in errors:
#             st.error(f"⚠️ {err}")
#     else:
#         st.success("🎉 Profile created successfully!")
#         st.balloons()

#         st.markdown("### ✅ Registered Profile")
#         fields = {
#             "Full Name":          name,
#             "Date of Birth":      dob.strftime("%d %B %Y") if dob else "—",
#             "Gender":             gender,
#             "Phone":              f"+91 {phone}",
#             "Email":              email,
#             "Preferred Language": language,
#             "Notifications":      notification_pref,
#             "ISL Speaker":        isl_speaker,
#         }
#         if isl_speaker == "Yes":
#             fields["ISL Experience"] = f"{isl_exp} year(s)"
#             fields["Proficiency"]    = isl_level
#         if bio.strip():
#             fields["Bio"] = bio.strip()

#         rows = "".join(
#             f'<div class="confirm-row">'
#             f'<span class="confirm-key">{k}</span>'
#             f'<span class="confirm-val">{v}</span>'
#             f'</div>'
#             for k, v in fields.items()
#         )
#         st.markdown(f'<div class="confirm-card">{rows}</div>', unsafe_allow_html=True)
# # ─── Sidebar ──────────────────────────────────────────────────────────────────
# with st.sidebar:
    

#     if st.session_state.get("logged_in"):
#         email_disp = st.session_state.get("user_email", "User")
#         name_disp  = st.session_state.get("user_name", email_disp.split("@")[0].title())
#         st.markdown(f"""
#         <div style="background:#ffffff; border:2px solid #A8E6CE; border-radius:4px;
#                     box-shadow:3px 3px 0px #8ed4b8; padding:1rem; margin-bottom:1rem;">
#             <div style="font-size:2rem; text-align:center; margin-bottom:.5rem;">Hi!</div>
#             <div style="font-weight:800; color:#2d3748; font-size:1rem; text-align:center;">{name_disp}</div>
#             <div style="font-size:.78rem; color:#718096; text-align:center;">{email_disp}</div>
#         </div>
#         """, unsafe_allow_html=True)

        

#         st.markdown("<hr style='border-color:#DCEDC2;'>", unsafe_allow_html=True)

#         if st.button("🚪  Logout"):
#             for key in ["logged_in", "user_email", "user_name"]:
#                 st.session_state.pop(key, None)
#             st.rerun()
    

#     st.markdown("<hr style='border-color:#DCEDC2;'>", unsafe_allow_html=True)
    
# import streamlit as st
# import re
# import datetime

# import streamlit as st
# import sqlite3

# conc= sqlite3.connect('form.db', check_same_thread=False)
# cursor=conn.cursor()

# # ─── Page config ─────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="Login / Register",
#     page_icon="👤",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ─── Load global CSS (mirrors utils/style.py load_css exactly) ───────────────
# from utils.style import load_css
# load_css()

# # ─── Extra styles scoped to this page only ───────────────────────────────────
# st.markdown("""
# <style>
# /* ── Page wrapper ── */
# .block-container { padding: 2rem 3rem !important; max-width: 900px !important; }

# /* ── Hero banner ── */
# .hero {
#     background: #ffffff;
#     padding: 2.2rem 2.8rem;
#     border-radius: 4px;
#     border: 2px solid #A8E6CE;
#     box-shadow: 6px 6px 0px #8ed4b8;
#     margin-bottom: 2rem;
#     position: relative;
#     overflow: hidden;
# }
# .hero::after {
#     content: '';
#     position: absolute;
#     top: -40px; right: -40px;
#     width: 160px; height: 160px;
#     background: #DCEDC2;
#     border-radius: 4px;
#     opacity: .45;
#     transform: rotate(20deg);
# }
# .hero-title {
#     font-size: 2.6rem;
#     font-weight: 800;
#     color: #2d3748;
#     letter-spacing: -0.5px;
#     margin: 0 0 .3rem;
# }
# .hero-title span { color: #FF8C94; }
# .hero-sub { color: #718096; font-size: .95rem; margin: 0; }

# /* ── Section labels ── */
# .section-label {
#     font-size: .7rem;
#     font-weight: 800;
#     letter-spacing: .2em;
#     text-transform: uppercase;
#     color: #FF8C94;
#     margin: 1.6rem 0 .7rem;
#     display: flex;
#     align-items: center;
#     gap: .6rem;
# }
# .section-label::after {
#     content: '';
#     flex: 1;
#     height: 2px;
#     background: #FFAAA6;
#     opacity: .4;
# }

# /* ── Tabs override ── */
# [data-testid="stTabs"] [role="tablist"] {
#     gap: 8px;
#     border-bottom: 2px solid #DCEDC2 !important;
#     margin-bottom: 1.6rem;
# }
# [data-testid="stTabs"] button[role="tab"] {
#     background: #ffffff !important;
#     border: 2px solid #DCEDC2 !important;
#     border-bottom: none !important;
#     border-radius: 4px 4px 0 0 !important;
#     color: #2d3748 !important;
#     font-size: 15px !important;
#     font-weight: 700 !important;
#     padding: 10px 28px !important;
#     box-shadow: 3px 0px 0px #e0e0e0 !important;
#     width: auto !important;
#     letter-spacing: .5px;
#     transition: all .15s ease !important;
#     text-transform: uppercase !important;
# }
# [data-testid="stTabs"] button[role="tab"]:hover {
#     background: #DCEDC2 !important;
#     transform: translate(-1px, -1px) !important;
#     box-shadow: 4px 0px 0px #c5d9a8 !important;
# }
# [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
#     background: linear-gradient(135deg, #FF8C94, #FFAAA6) !important;
#     border-color: #FF8C94 !important;
#     color: #2d3748 !important;
#     box-shadow: 4px 0px 0px #e07a82 !important;
#     transform: translate(-2px, -2px) !important;
# }

# /* ── Input overrides ── */
# [data-testid="stTextInput"] > div > div,
# [data-testid="stNumberInput"] > div > div,
# [data-testid="stDateInput"] > div > div {
#     background: #fefefe !important;
#     border: 2px solid #DCEDC2 !important;
#     border-radius: 4px !important;
#     transition: border-color .2s, box-shadow .2s;
# }
# [data-testid="stTextInput"] > div > div:focus-within,
# [data-testid="stNumberInput"] > div > div:focus-within,
# [data-testid="stDateInput"] > div > div:focus-within {
#     border-color: #A8E6CE !important;
#     box-shadow: 0 0 0 3px rgba(168,230,206,.35) !important;
# }
# [data-testid="stTextInput"] input,
# [data-testid="stNumberInput"] input { color: #2d3748 !important; font-size: 15px !important; }

# /* Labels */
# label[data-testid="stWidgetLabel"] p {
#     color: #2d3748 !important;
#     font-size: .92rem !important;
#     font-weight: 600 !important;
# }

# /* Radio */
# [data-testid="stRadio"] label {
#     background: transparent !important;
#     border: none !important;
#     box-shadow: none !important;
#     font-size: .92rem !important;
#     font-weight: 500 !important;
#     color: #2d3748 !important;
# }
# [data-testid="stRadio"] label:has(input:checked) {
#     color: #FF8C94 !important;
#     font-weight: 700 !important;
# }
# [data-testid="stRadio"] input {
#     display: inline-block !important;
#     accent-color: #FF8C94 !important;
#     width: 15px !important; height: 15px !important;
#     margin-right: 4px !important;
# }

# /* Selectbox */
# [data-testid="stSelectbox"] > div > div {
#     background: #fefefe !important;
#     border: 2px solid #DCEDC2 !important;
#     border-radius: 4px !important;
#     color: #2d3748 !important;
# }

# /* Slider accent */
# [data-testid="stSlider"] [role="slider"] {
#     background: #FF8C94 !important;
#     border-color: #FF8C94 !important;
# }

# /* Checkbox */
# [data-testid="stCheckbox"] label { font-weight: 600 !important; color: #2d3748 !important; }

# /* Password show/hide eye button — force square */
# [data-testid="stTextInput"] button {
#     width: 36px !important;
#     min-width: 36px !important;
#     max-width: 36px !important;
#     padding: 0 !important;
#     border-radius: 4px !important;
#     box-shadow: none !important;
#     border: none !important;
#     background: transparent !important;
#     flex-shrink: 0 !important;
# }
# [data-testid="stTextInput"] button:hover {
#     background: #DCEDC2 !important;
#     transform: none !important;
#     box-shadow: none !important;
# }

# /* Submit button */
# [data-testid="stFormSubmitButton"] button {
#     background: linear-gradient(135deg, #FF8C94, #FFAAA6) !important;
#     color: #2d3748 !important;
#     font-size: 16px !important;
#     font-weight: 800 !important;
#     padding: 14px 28px !important;
#     border-radius: 4px !important;
#     border: 2px solid #FF8C94 !important;
#     box-shadow: 4px 4px 0px #e07a82 !important;
#     transition: all .15s ease !important;
#     width: 100% !important;
#     text-transform: uppercase !important;
#     letter-spacing: 1px !important;
#     margin-top: 1rem !important;
# }
# [data-testid="stFormSubmitButton"] button:hover {
#     transform: translate(-2px,-2px) !important;
#     box-shadow: 6px 6px 0px #e07a82 !important;
#     background: linear-gradient(135deg, #FFAAA6, #FFD3B5) !important;
# }
# [data-testid="stFormSubmitButton"] button:active {
#     transform: translate(2px,2px) !important;
#     box-shadow: 2px 2px 0px #e07a82 !important;
# }

# /* Char counter */
# .char-count { font-size: .72rem; color: #718096; text-align: right; margin-top: .15rem; font-weight: 600; }
# .char-ok    { color: #5cb88a; }
# .char-bad   { color: #e85d6c; }

# /* Confirmation card */
# .confirm-card {
#     background: #ffffff;
#     border: 2px solid #A8E6CE;
#     border-radius: 4px;
#     box-shadow: 6px 6px 0px #8ed4b8;
#     padding: 1.6rem 2rem;
#     margin-top: 1.2rem;
# }
# .confirm-row {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     padding: .5rem 0;
#     border-bottom: 1px solid #DCEDC2;
#     font-size: .9rem;
# }
# .confirm-row:last-child { border-bottom: none; }
# .confirm-key { color: #e85d6c; font-weight: 700; }
# .confirm-val { color: #2d3748; font-weight: 600; }

# /* Progress bar */
# .prog-wrap  { margin: .5rem 0 1.2rem; }
# .prog-label { font-size: .78rem; color: #718096; font-weight: 700; margin-bottom: .35rem; }
# .prog-bar-bg {
#     background: rgba(0,0,0,.08);
#     border-radius: 4px;
#     height: 8px;
#     overflow: hidden;
#     border: 1px solid rgba(0,0,0,.06);
# }
# .prog-bar-fill { height: 100%; border-radius: 4px; transition: width .4s ease, background .4s; }

# /* Divider */
# hr.styled { border: none; border-top: 2px solid #DCEDC2; margin: 1.4rem 0; opacity: .7; }

# /* Welcome badge (login success) */
# .welcome-badge {
#     background: #ffffff;
#     border: 2px solid #A8E6CE;
#     border-radius: 4px;
#     box-shadow: 5px 5px 0px #8ed4b8;
#     padding: 1.4rem 2rem;
#     display: flex;
#     align-items: center;
#     gap: 1rem;
#     margin-bottom: 1.2rem;
# }
# .welcome-badge .avatar {
#     width: 52px; height: 52px;
#     background: linear-gradient(135deg, #FF8C94, #FFAAA6);
#     border-radius: 4px;
#     border: 2px solid #FF8C94;
#     display: flex; align-items: center; justify-content: center;
#     font-size: 1.4rem;
#     box-shadow: 3px 3px 0px #e07a82;
#     flex-shrink: 0;
# }
# .welcome-badge .info { flex: 1; }
# .welcome-badge .info strong { font-size: 1.1rem; font-weight: 800; color: #2d3748; display: block; }
# .welcome-badge .info span  { font-size: .85rem; color: #718096; }
# </style>
# """, unsafe_allow_html=True)

# # ─── Validators ───────────────────────────────────────────────────────────────
# def is_valid_email(email: str) -> bool:
#     return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$", email))

# def is_valid_phone(phone: str) -> bool:
#     return bool(re.match(r"^\d{10}$", phone))

# def is_valid_name(name: str) -> bool:
#     return bool(name) and len(name.strip()) >= 2

# def completion_score(fv: dict) -> int:
#     fields = ["name", "dob", "gender", "phone", "email", "language", "ISLSpeaker"]
#     filled = sum(1 for f in fields if fv.get(f) not in [None, "", 0])
#     return int(filled / len(fields) * 100)

# def progress_html(pct: int) -> str:
#     if pct < 40:
#         colour, label = "#e85d6c", "Just getting started…"
#     elif pct < 75:
#         colour, label = "#f59e0b", f"{pct}% — Keep going!"
#     else:
#         colour = "#5cb88a"
#         label  = f"{pct}% — Almost there!" if pct < 100 else "✅ 100% — Ready to submit!"
#     return f"""
#     <div class="prog-wrap">
#         <div class="prog-label">Form completion · {label}</div>
#         <div class="prog-bar-bg">
#             <div class="prog-bar-fill" style="width:{pct}%; background:{colour};"></div>
#         </div>
#     </div>"""

# # ─── Sidebar ──────────────────────────────────────────────────────────────────
# with st.sidebar:
#     # st.markdown("## 👤 Account")
#     # st.markdown("---")

#     if st.session_state.get("logged_in"):
#         email_disp = st.session_state.get("user_email", "User")
#         name_disp  = st.session_state.get("user_name", email_disp.split("@")[0].title())
#         st.markdown(f"""
#         <div style="background:#ffffff; border:2px solid #A8E6CE; border-radius:4px;
#                     box-shadow:3px 3px 0px #8ed4b8; padding:1rem; margin-bottom:1rem;">
#             <div style="font-size:2rem; text-align:center; margin-bottom:.5rem;">👋</div>
#             <div style="font-weight:800; color:#2d3748; font-size:1rem; text-align:center;">{name_disp}</div>
#             <div style="font-size:.78rem; color:#718096; text-align:center;">{email_disp}</div>
#         </div>
#         """, unsafe_allow_html=True)

#         # if st.button("🚀  Go to Translator"):
#         #     st.switch_page("pages/main.py")

#         # st.markdown("<hr style='border-color:#DCEDC2;'>", unsafe_allow_html=True)

#         if st.button("🚪  Logout"):
#             for key in ["logged_in", "user_email", "user_name"]:
#                 st.session_state.pop(key, None)
#     #         st.rerun()
#     # else:
#     #     st.markdown("""
#     #     <div style="background:#ffffff; border:2px solid #DCEDC2; border-radius:4px;
#     #                 padding:1rem; font-size:.88rem; color:#718096; line-height:1.6;">
#     #         🔑 <strong style="color:#FF8C94;">Login</strong> to access the<br>
#     #         Hindi → ISL Translator and save your preferences.
#     #     </div>
#     #     """, unsafe_allow_html=True)

#     #     st.markdown("<hr style='border-color:#DCEDC2;'>", unsafe_allow_html=True)
#     #     st.markdown("### 📌 Quick Links")

#     #     if st.button("🏠  Home"):
#     #         st.switch_page("app.py")
#     #     if st.button("ℹ️  About"):
#     #         st.switch_page("pages/about.py")

#     # st.markdown("<hr style='border-color:#DCEDC2;'>", unsafe_allow_html=True)
#     # st.markdown("""
#     # <div style="font-size:.75rem; color:#a0aec0; line-height:1.8;">
#     #     <strong style="color:#FF8C94;">Hindi to ISL</strong><br>
#     #     Bridging spoken Hindi and<br>
#     #     Indian Sign Language.<br><br>
#     #     🌐 Inclusive · ✨ Accessible
#     # </div>
#     # """, unsafe_allow_html=True)

# # ─── Hero ─────────────────────────────────────────────────────────────────────
# if st.session_state.get("logged_in"):
#     name_disp  = st.session_state.get("user_name", "there")
#     email_disp = st.session_state.get("user_email", "")
#     st.markdown(f"""
#     <div class="hero">
#         <p class="hero-title">Welcome back, <span>{name_disp}</span> 👋</p>
#         <p class="hero-sub">You are signed in as {email_disp}. Ready to translate?</p>
#     </div>
#     """, unsafe_allow_html=True)
#     if st.button("🚀  Open Translator"):
#         st.switch_page("pages/main.py")
#     st.stop()

# st.markdown("""
# <div class="hero">
#     <p class="hero-title">Your <span>Account</span></p>
#     <p class="hero-sub">Sign in to your existing profile or create a new one below.</p>
# </div>
# """, unsafe_allow_html=True)

# # ─── Tabs: Login | Register ────────────────────────────────────────────────────
# tab_login, tab_register = st.tabs(["🔑   Login", "📝   Register"])

# # ══════════════════════════════════════════════════════════════════════════════
# # TAB 1 — LOGIN
# # ══════════════════════════════════════════════════════════════════════════════
# with tab_login:
#     col_main, col_gap = st.columns([2, 1], gap="large")

#     with col_main:
#         st.markdown('<div class="section-label">🔐 Sign in to your account</div>', unsafe_allow_html=True)

#         with st.form("loginForm"):
#             login_email    = st.text_input("Email Address", placeholder="you@example.com", max_chars=80)
#             login_password = st.text_input("Password", type="password", placeholder="••••••••")
#             login_submit   = st.form_submit_button("🔑  Sign In")

#         if login_submit:
#             if not login_email or not login_password:
#                 st.error("⚠️ Please enter both your email and password.")
#             elif not is_valid_email(login_email):
#                 st.error("⚠️ Please enter a valid email address.")
#             elif len(login_password) < 6:
#                 st.error("⚠️ Password must be at least 6 characters.")
#             else:
#                 # ── Replace this block with real auth (Firebase / Supabase / DB) ──
#                 st.session_state["logged_in"]  = True
#                 st.session_state["user_email"] = login_email
#                 st.session_state["user_name"]  = login_email.split("@")[0].title()
#                 st.success("🎉 Signed in successfully!")
#                 st.balloons()
#                 st.rerun()

#     with col_gap:
#         st.markdown("""
#         <div class="card" style="margin-top:2.2rem;">
#             <div style="font-size:1.8rem; margin-bottom:.6rem;">💡</div>
#             <strong style="color:#FF8C94; font-size:.85rem; text-transform:uppercase; letter-spacing:.1em;">New here?</strong>
#             <p style="font-size:.88rem; color:#718096; margin-top:.4rem; line-height:1.6;">
#                 Switch to the <strong>Register</strong> tab to create your free ISL Translator profile.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════════════════════════════
# # TAB 2 — REGISTER
# # ══════════════════════════════════════════════════════════════════════════════
# with tab_register:
#     st.markdown('<div class="section-label">✨ Create your profile</div>', unsafe_allow_html=True)

#     with st.form(key="registerForm", clear_on_submit=False):

#         # ── Personal Info ──────────────────────────────────────────────────────
#         st.markdown('<div class="section-label">👤 Personal Information</div>', unsafe_allow_html=True)

#         r_col1, r_col2 = st.columns(2, gap="large")
#         with r_col1:
#             r_name = st.text_input("Full Name *", placeholder="e.g. Ayushi Sharma",
#                                    max_chars=60, key="r_name")
#             name_ok  = is_valid_name(r_name)
#             name_cls = "char-ok" if name_ok else ("char-bad" if r_name else "")
#             st.markdown(f'<div class="char-count {name_cls}">{len(r_name)}/60'
#                         + (' ✓' if name_ok else '') + '</div>', unsafe_allow_html=True)

#         with r_col2:
#             r_gender = st.radio("Gender *", ["Male", "Female", "Prefer not to say"],
#                                 horizontal=True, key="r_gender")

#         r_dob = st.date_input(
#             "Date of Birth *", value=None,
#             min_value=datetime.date(1900, 1, 1),
#             max_value=datetime.date.today(),
#             format="DD/MM/YYYY", key="r_dob"
#         )

#         # ── Contact ────────────────────────────────────────────────────────────
#         st.markdown('<div class="section-label">📬 Contact Details</div>', unsafe_allow_html=True)

#         r_col3, r_col4 = st.columns(2, gap="large")
#         with r_col3:
#             r_phone = st.text_input("Phone Number * (10 digits)", placeholder="9876543210",
#                                     max_chars=10, key="r_phone")
#             phone_ok = is_valid_phone(r_phone)
#             ph_cls   = "char-ok" if phone_ok else ("char-bad" if r_phone else "")
#             st.markdown(f'<div class="char-count {ph_cls}">{len(r_phone)}/10'
#                         + (' ✓' if phone_ok else '') + '</div>', unsafe_allow_html=True)

#         with r_col4:
#             r_email = st.text_input("Email Address *", placeholder="you@example.com",
#                                     max_chars=80, key="r_email")
#             email_ok = is_valid_email(r_email)
#             em_cls   = "char-ok" if email_ok else ("char-bad" if r_email else "")
#             st.markdown(f'<div class="char-count {em_cls}">'
#                         + ('Valid ✓' if email_ok else (f'{len(r_email)}/80' if r_email else ''))
#                         + '</div>', unsafe_allow_html=True)

#         r_col5, r_col6 = st.columns(2, gap="large")
#         with r_col5:
#             r_password = st.text_input("Create Password *", type="password",
#                                        placeholder="min 6 characters", key="r_password")
#             pw_ok  = len(r_password) >= 6
#             pw_cls = "char-ok" if pw_ok else ("char-bad" if r_password else "")
#             st.markdown(f'<div class="char-count {pw_cls}">'
#                         + ('Strong enough ✓' if pw_ok else ('Too short' if r_password else ''))
#                         + '</div>', unsafe_allow_html=True)

#         with r_col6:
#             r_password2 = st.text_input("Confirm Password *", type="password",
#                                         placeholder="repeat password", key="r_password2")
#             match_ok  = r_password and r_password == r_password2
#             match_cls = "char-ok" if match_ok else ("char-bad" if r_password2 else "")
#             st.markdown(f'<div class="char-count {match_cls}">'
#                         + ('Passwords match ✓' if match_ok else ('Mismatch ✗' if r_password2 else ''))
#                         + '</div>', unsafe_allow_html=True)

#         # ── Preferences & ISL ─────────────────────────────────────────────────
#         st.markdown('<div class="section-label">🌐 Preferences & ISL</div>', unsafe_allow_html=True)

#         r_col7, r_col8 = st.columns(2, gap="large")
#         with r_col7:
#             r_language = st.selectbox("Preferred Language *",
#                             ["English", "Hindi", "Tamil", "Telugu",
#                              "Kannada", "Bengali", "Marathi", "Gujarati"],
#                             key="r_language")
#             r_notif = st.radio("Notification Preference",
#                                ["Email", "SMS", "None"], horizontal=True, key="r_notif")

#         with r_col8:
#             r_isl = st.radio("Have you learned ISL? *", ["Yes", "No"],
#                              horizontal=True, key="r_isl")
#             if r_isl == "Yes":
#                 r_isl_exp   = st.slider("Years of ISL Experience", 0, 40, 1, key="r_isl_exp")
#                 r_isl_level = st.selectbox("Proficiency Level",
#                                 ["Beginner", "Elementary", "Intermediate", "Advanced", "Fluent"],
#                                 key="r_isl_level")
#             else:
#                 r_isl_exp, r_isl_level = 0, None

#         # ── Bio ───────────────────────────────────────────────────────────────
#         st.markdown('<div class="section-label">📝 Short Bio (Optional)</div>', unsafe_allow_html=True)
#         r_bio = st.text_area("Tell us a little about yourself",
#                              placeholder="I am a teacher who works with the deaf community…",
#                              max_chars=300, height=90, key="r_bio")
#         bio_cls = "char-ok" if 10 <= len(r_bio) <= 300 else ("char-bad" if len(r_bio) > 300 else "")
#         st.markdown(f'<div class="char-count {bio_cls}">{len(r_bio)}/300</div>',
#                     unsafe_allow_html=True)

#         # ── Terms & progress ──────────────────────────────────────────────────
#         st.markdown("<hr class='styled'>", unsafe_allow_html=True)
#         r_agree = st.checkbox("I agree to the Terms & Conditions and Privacy Policy *",
#                               key="r_agree")

#         score = completion_score({
#             "name": r_name, "dob": r_dob, "gender": r_gender,
#             "phone": r_phone, "email": r_email,
#             "language": r_language, "ISLSpeaker": r_isl,
#         })
#         st.markdown(progress_html(score), unsafe_allow_html=True)

#         reg_submit = st.form_submit_button("🚀  Create Profile")

#     # ── Validation & success ──────────────────────────────────────────────────
#     if reg_submit:
#         errors = []
#         if not is_valid_name(r_name):          errors.append("Name must be at least 2 characters.")
#         if not r_dob:                           errors.append("Please provide your Date of Birth.")
#         if not is_valid_phone(r_phone):         errors.append("Phone number must be exactly 10 digits.")
#         if not is_valid_email(r_email):         errors.append("Please enter a valid email address.")
#         if len(r_password) < 6:                 errors.append("Password must be at least 6 characters.")
#         if r_password != r_password2:           errors.append("Passwords do not match.")
#         if not r_agree:                         errors.append("You must accept the Terms & Conditions.")

#         if errors:
#             for err in errors:
#                 st.error(f"⚠️ {err}")
#         else:
#             # ── Store in session (replace with real DB write) ──
#             st.session_state["logged_in"]  = True
#             st.session_state["user_email"] = r_email
#             st.session_state["user_name"]  = r_name.strip()

#             st.success("🎉 Profile created successfully! You are now logged in.")
#             st.balloons()

#             # Confirmation card
#             fields = {
#                 "Full Name":          r_name,
#                 "Date of Birth":      r_dob.strftime("%d %B %Y") if r_dob else "—",
#                 "Gender":             r_gender,
#                 "Phone":              f"+91 {r_phone}",
#                 "Email":              r_email,
#                 "Preferred Language": r_language,
#                 "Notifications":      r_notif,
#                 "ISL Speaker":        r_isl,
#             }
#             if r_isl == "Yes":
#                 fields["ISL Experience"] = f"{r_isl_exp} year(s)"
#                 fields["Proficiency"]    = r_isl_level
#             if r_bio.strip():
#                 fields["Bio"] = r_bio.strip()

#             rows = "".join(
#                 f'<div class="confirm-row">'
#                 f'<span class="confirm-key">{k}</span>'
#                 f'<span class="confirm-val">{v}</span>'
#                 f'</div>'
#                 for k, v in fields.items()
#             )
#             st.markdown(f"""
#             <div style="margin-top:1rem;">
#                 <strong style="color:#FF8C94;">✅ Registered Profile</strong>
#             </div>
#             <div class="confirm-card">{rows}</div>
#             """, unsafe_allow_html=True)

#             col_btn, _ = st.columns([1, 2])
#             with col_btn:
#                 if st.button("🚀  Go to Translator"):
#                     st.switch_page("pages/main.py")


import streamlit as st
import re
import datetime
import sqlite3
import hashlib
import os

# ─── Database Setup ──────────────────────────────────────────────────────────
# Dynamically get the path to the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'form.db')

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT,
            name TEXT,
            gender TEXT,
            dob TEXT,
            phone TEXT,
            language TEXT,
            notif TEXT,
            isl_speaker TEXT,
            isl_exp INTEGER,
            isl_level TEXT,
            bio TEXT
        )
    ''')
    conn.commit()

init_db()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# ─── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Login / Register",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Load global CSS (mirrors utils/style.py load_css exactly) ───────────────
try:
    from utils.style import load_css
    load_css()
except ImportError:
    pass # Ignored if running standalone without the utils package

# ─── Extra styles scoped to this page only ───────────────────────────────────
st.markdown("""
<style>
/* ── Page wrapper ── */
.block-container { padding: 2rem 3rem !important; max-width: 900px !important; }

/* ── Hero banner ── */
.hero {
    background: #ffffff;
    padding: 2.2rem 2.8rem;
    border-radius: 4px;
    border: 2px solid #A8E6CE;
    box-shadow: 6px 6px 0px #8ed4b8;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 160px; height: 160px;
    background: #DCEDC2;
    border-radius: 4px;
    opacity: .45;
    transform: rotate(20deg);
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #2d3748;
    letter-spacing: -0.5px;
    margin: 0 0 .3rem;
}
.hero-title span { color: #FF8C94; }
.hero-sub { color: #718096; font-size: .95rem; margin: 0; }

/* ── Section labels ── */
.section-label {
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: #FF8C94;
    margin: 1.6rem 0 .7rem;
    display: flex;
    align-items: center;
    gap: .6rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 2px;
    background: #FFAAA6;
    opacity: .4;
}

/* ── Tabs override ── */
[data-testid="stTabs"] [role="tablist"] {
    gap: 8px;
    border-bottom: 2px solid #DCEDC2 !important;
    margin-bottom: 1.6rem;
}
[data-testid="stTabs"] button[role="tab"] {
    background: #ffffff !important;
    border: 2px solid #DCEDC2 !important;
    border-bottom: none !important;
    border-radius: 4px 4px 0 0 !important;
    color: #2d3748 !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    padding: 10px 28px !important;
    box-shadow: 3px 0px 0px #e0e0e0 !important;
    width: auto !important;
    letter-spacing: .5px;
    transition: all .15s ease !important;
    text-transform: uppercase !important;
}
[data-testid="stTabs"] button[role="tab"]:hover {
    background: #DCEDC2 !important;
    transform: translate(-1px, -1px) !important;
    box-shadow: 4px 0px 0px #c5d9a8 !important;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    background: linear-gradient(135deg, #FF8C94, #FFAAA6) !important;
    border-color: #FF8C94 !important;
    color: #2d3748 !important;
    box-shadow: 4px 0px 0px #e07a82 !important;
    transform: translate(-2px, -2px) !important;
}

/* ── Input overrides ── */
[data-testid="stTextInput"] > div > div,
[data-testid="stNumberInput"] > div > div,
[data-testid="stDateInput"] > div > div {
    background: #fefefe !important;
    border: 2px solid #DCEDC2 !important;
    border-radius: 4px !important;
    transition: border-color .2s, box-shadow .2s;
}
[data-testid="stTextInput"] > div > div:focus-within,
[data-testid="stNumberInput"] > div > div:focus-within,
[data-testid="stDateInput"] > div > div:focus-within {
    border-color: #A8E6CE !important;
    box-shadow: 0 0 0 3px rgba(168,230,206,.35) !important;
}
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input { color: #2d3748 !important; font-size: 15px !important; }

/* Labels */
label[data-testid="stWidgetLabel"] p {
    color: #2d3748 !important;
    font-size: .92rem !important;
    font-weight: 600 !important;
}

/* Radio */
[data-testid="stRadio"] label {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: .92rem !important;
    font-weight: 500 !important;
    color: #2d3748 !important;
}
[data-testid="stRadio"] label:has(input:checked) {
    color: #FF8C94 !important;
    font-weight: 700 !important;
}
[data-testid="stRadio"] input {
    display: inline-block !important;
    accent-color: #FF8C94 !important;
    width: 15px !important; height: 15px !important;
    margin-right: 4px !important;
}

/* Selectbox */
[data-testid="stSelectbox"] > div > div {
    background: #fefefe !important;
    border: 2px solid #DCEDC2 !important;
    border-radius: 4px !important;
    color: #2d3748 !important;
}

/* Slider accent */
[data-testid="stSlider"] [role="slider"] {
    background: #FF8C94 !important;
    border-color: #FF8C94 !important;
}

/* Checkbox */
[data-testid="stCheckbox"] label { font-weight: 600 !important; color: #2d3748 !important; }

/* Password show/hide eye button — force square */
[data-testid="stTextInput"] button {
    width: 36px !important;
    min-width: 36px !important;
    max-width: 36px !important;
    padding: 0 !important;
    border-radius: 4px !important;
    box-shadow: none !important;
    border: none !important;
    background: transparent !important;
    flex-shrink: 0 !important;
}
[data-testid="stTextInput"] button:hover {
    background: #DCEDC2 !important;
    transform: none !important;
    box-shadow: none !important;
}

/* Submit button */
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #FF8C94, #FFAAA6) !important;
    color: #2d3748 !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    padding: 14px 28px !important;
    border-radius: 4px !important;
    border: 2px solid #FF8C94 !important;
    box-shadow: 4px 4px 0px #e07a82 !important;
    transition: all .15s ease !important;
    width: 100% !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    margin-top: 1rem !important;
}
[data-testid="stFormSubmitButton"] button:hover {
    transform: translate(-2px,-2px) !important;
    box-shadow: 6px 6px 0px #e07a82 !important;
    background: linear-gradient(135deg, #FFAAA6, #FFD3B5) !important;
}
[data-testid="stFormSubmitButton"] button:active {
    transform: translate(2px,2px) !important;
    box-shadow: 2px 2px 0px #e07a82 !important;
}

/* Char counter */
.char-count { font-size: .72rem; color: #718096; text-align: right; margin-top: .15rem; font-weight: 600; }
.char-ok    { color: #5cb88a; }
.char-bad   { color: #e85d6c; }

/* Confirmation card */
.confirm-card {
    background: #ffffff;
    border: 2px solid #A8E6CE;
    border-radius: 4px;
    box-shadow: 6px 6px 0px #8ed4b8;
    padding: 1.6rem 2rem;
    margin-top: 1.2rem;
}
.confirm-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: .5rem 0;
    border-bottom: 1px solid #DCEDC2;
    font-size: .9rem;
}
.confirm-row:last-child { border-bottom: none; }
.confirm-key { color: #e85d6c; font-weight: 700; }
.confirm-val { color: #2d3748; font-weight: 600; }

/* Progress bar */
.prog-wrap  { margin: .5rem 0 1.2rem; }
.prog-label { font-size: .78rem; color: #718096; font-weight: 700; margin-bottom: .35rem; }
.prog-bar-bg {
    background: rgba(0,0,0,.08);
    border-radius: 4px;
    height: 8px;
    overflow: hidden;
    border: 1px solid rgba(0,0,0,.06);
}
.prog-bar-fill { height: 100%; border-radius: 4px; transition: width .4s ease, background .4s; }

/* Divider */
hr.styled { border: none; border-top: 2px solid #DCEDC2; margin: 1.4rem 0; opacity: .7; }

/* Welcome badge (login success) */
.welcome-badge {
    background: #ffffff;
    border: 2px solid #A8E6CE;
    border-radius: 4px;
    box-shadow: 5px 5px 0px #8ed4b8;
    padding: 1.4rem 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.2rem;
}
.welcome-badge .avatar {
    width: 52px; height: 52px;
    background: linear-gradient(135deg, #FF8C94, #FFAAA6);
    border-radius: 4px;
    border: 2px solid #FF8C94;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    box-shadow: 3px 3px 0px #e07a82;
    flex-shrink: 0;
}
.welcome-badge .info { flex: 1; }
.welcome-badge .info strong { font-size: 1.1rem; font-weight: 800; color: #2d3748; display: block; }
.welcome-badge .info span  { font-size: .85rem; color: #718096; }
</style>
""", unsafe_allow_html=True)

# ─── Validators ───────────────────────────────────────────────────────────────
def is_valid_email(email: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]{2,}$", email))

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(r"^\d{10}$", phone))

def is_valid_name(name: str) -> bool:
    return bool(name) and len(name.strip()) >= 2

def completion_score(fv: dict) -> int:
    fields = ["name", "dob", "gender", "phone", "email", "language", "ISLSpeaker"]
    filled = sum(1 for f in fields if fv.get(f) not in [None, "", 0])
    return int(filled / len(fields) * 100)

def progress_html(pct: int) -> str:
    if pct < 40:
        colour, label = "#e85d6c", "Just getting started…"
    elif pct < 75:
        colour, label = "#f59e0b", f"{pct}% — Keep going!"
    else:
        colour = "#5cb88a"
        label  = f"{pct}% — Almost there!" if pct < 100 else "✅ 100% — Ready to submit!"
    return f"""
    <div class="prog-wrap">
        <div class="prog-label">Form completion · {label}</div>
        <div class="prog-bar-bg">
            <div class="prog-bar-fill" style="width:{pct}%; background:{colour};"></div>
        </div>
    </div>"""

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    if st.session_state.get("logged_in"):
        email_disp = st.session_state.get("user_email", "User")
        name_disp  = st.session_state.get("user_name", email_disp.split("@")[0].title())
        st.markdown(f"""
        <div style="background:#ffffff; border:2px solid #A8E6CE; border-radius:4px;
                    box-shadow:3px 3px 0px #8ed4b8; padding:1rem; margin-bottom:1rem;">
            <div style="font-size:2rem; text-align:center; margin-bottom:.5rem;">👋</div>
            <div style="font-weight:800; color:#2d3748; font-size:1rem; text-align:center;">{name_disp}</div>
            <div style="font-size:.78rem; color:#718096; text-align:center;">{email_disp}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚪  Logout"):
            for key in ["logged_in", "user_email", "user_name"]:
                st.session_state.pop(key, None)
            st.rerun()

# ─── Hero ─────────────────────────────────────────────────────────────────────
if st.session_state.get("logged_in"):
    name_disp  = st.session_state.get("user_name", "there")
    email_disp = st.session_state.get("user_email", "")
    st.markdown(f"""
    <div class="hero">
        <p class="hero-title">Welcome back, <span>{name_disp}</span> 👋</p>
        <p class="hero-sub">You are signed in as {email_disp}. Ready to translate?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀  Open Translator"):
        st.switch_page("pages/main.py")
    st.stop()

st.markdown("""
<div class="hero">
    <p class="hero-title">Your <span>Account</span></p>
    <p class="hero-sub">Sign in to your existing profile or create a new one below.</p>
</div>
""", unsafe_allow_html=True)

# ─── Tabs: Login | Register ────────────────────────────────────────────────────
tab_login, tab_register = st.tabs(["🔑   Login", "📝   Register"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — LOGIN
# ══════════════════════════════════════════════════════════════════════════════
with tab_login:
    col_main, col_gap = st.columns([2, 1], gap="large")

    with col_main:
        st.markdown('<div class="section-label">🔐 Sign in to your account</div>', unsafe_allow_html=True)

        with st.form("loginForm"):
            login_email    = st.text_input("Email Address", placeholder="you@example.com", max_chars=80)
            login_password = st.text_input("Password", type="password", placeholder="••••••••")
            login_submit   = st.form_submit_button("🔑  Sign In")

        if login_submit:
            if not login_email or not login_password:
                st.error("⚠️ Please enter both your email and password.")
            elif not is_valid_email(login_email):
                st.error("⚠️ Please enter a valid email address.")
            else:
                # ── Database Retrieval ──
                cursor.execute("SELECT name, password FROM users WHERE email = ?", (login_email,))
                user_record = cursor.fetchone()
                
                if user_record and user_record[1] == hash_password(login_password):
                    st.session_state["logged_in"]  = True
                    st.session_state["user_email"] = login_email
                    st.session_state["user_name"]  = user_record[0]
                    st.success("🎉 Signed in successfully!")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("⚠️ Invalid email or password. Please try again.")

    with col_gap:
        st.markdown("""
        <div class="card" style="margin-top:2.2rem;">
            <div style="font-size:1.8rem; margin-bottom:.6rem;">💡</div>
            <strong style="color:#FF8C94; font-size:.85rem; text-transform:uppercase; letter-spacing:.1em;">New here?</strong>
            <p style="font-size:.88rem; color:#718096; margin-top:.4rem; line-height:1.6;">
                Switch to the <strong>Register</strong> tab to create your free ISL Translator profile.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — REGISTER
# ══════════════════════════════════════════════════════════════════════════════
with tab_register:
    st.markdown('<div class="section-label">✨ Create your profile</div>', unsafe_allow_html=True)

    with st.form(key="registerForm", clear_on_submit=False):

        # ── Personal Info ──────────────────────────────────────────────────────
        st.markdown('<div class="section-label">👤 Personal Information</div>', unsafe_allow_html=True)

        r_col1, r_col2 = st.columns(2, gap="large")
        with r_col1:
            r_name = st.text_input("Full Name *", placeholder="e.g. Ayushi Sharma",
                                   max_chars=60, key="r_name")
            name_ok  = is_valid_name(r_name)
            name_cls = "char-ok" if name_ok else ("char-bad" if r_name else "")
            st.markdown(f'<div class="char-count {name_cls}">{len(r_name)}/60'
                        + (' ✓' if name_ok else '') + '</div>', unsafe_allow_html=True)

        with r_col2:
            r_gender = st.radio("Gender *", ["Male", "Female", "Prefer not to say"],
                                horizontal=True, key="r_gender")

        r_dob = st.date_input(
            "Date of Birth *", value=None,
            min_value=datetime.date(1900, 1, 1),
            max_value=datetime.date.today(),
            format="DD/MM/YYYY", key="r_dob"
        )

        # ── Contact ────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">📬 Contact Details</div>', unsafe_allow_html=True)

        r_col3, r_col4 = st.columns(2, gap="large")
        with r_col3:
            r_phone = st.text_input("Phone Number * (10 digits)", placeholder="9876543210",
                                    max_chars=10, key="r_phone")
            phone_ok = is_valid_phone(r_phone)
            ph_cls   = "char-ok" if phone_ok else ("char-bad" if r_phone else "")
            st.markdown(f'<div class="char-count {ph_cls}">{len(r_phone)}/10'
                        + (' ✓' if phone_ok else '') + '</div>', unsafe_allow_html=True)

        with r_col4:
            r_email = st.text_input("Email Address *", placeholder="you@example.com",
                                    max_chars=80, key="r_email")
            email_ok = is_valid_email(r_email)
            em_cls   = "char-ok" if email_ok else ("char-bad" if r_email else "")
            st.markdown(f'<div class="char-count {em_cls}">'
                        + ('Valid ✓' if email_ok else (f'{len(r_email)}/80' if r_email else ''))
                        + '</div>', unsafe_allow_html=True)

        r_col5, r_col6 = st.columns(2, gap="large")
        with r_col5:
            r_password = st.text_input("Create Password *", type="password",
                                       placeholder="min 6 characters", key="r_password")
            pw_ok  = len(r_password) >= 6
            pw_cls = "char-ok" if pw_ok else ("char-bad" if r_password else "")
            st.markdown(f'<div class="char-count {pw_cls}">'
                        + ('Strong enough ✓' if pw_ok else ('Too short' if r_password else ''))
                        + '</div>', unsafe_allow_html=True)

        with r_col6:
            r_password2 = st.text_input("Confirm Password *", type="password",
                                        placeholder="repeat password", key="r_password2")
            match_ok  = r_password and r_password == r_password2
            match_cls = "char-ok" if match_ok else ("char-bad" if r_password2 else "")
            st.markdown(f'<div class="char-count {match_cls}">'
                        + ('Passwords match ✓' if match_ok else ('Mismatch ✗' if r_password2 else ''))
                        + '</div>', unsafe_allow_html=True)

        # ── Preferences & ISL ─────────────────────────────────────────────────
        st.markdown('<div class="section-label">🌐 Preferences & ISL</div>', unsafe_allow_html=True)

        r_col7, r_col8 = st.columns(2, gap="large")
        with r_col7:
            r_language = st.selectbox("Preferred Language *",
                            ["English", "Hindi", "Tamil", "Telugu",
                             "Kannada", "Bengali", "Marathi", "Gujarati"],
                            key="r_language")
            r_notif = st.radio("Notification Preference",
                               ["Email", "SMS", "None"], horizontal=True, key="r_notif")

        with r_col8:
            r_isl = st.radio("Have you learned ISL? *", ["Yes", "No"],
                             horizontal=True, key="r_isl")
            if r_isl == "Yes":
                r_isl_exp   = st.slider("Years of ISL Experience", 0, 40, 1, key="r_isl_exp")
                r_isl_level = st.selectbox("Proficiency Level",
                                ["Beginner", "Elementary", "Intermediate", "Advanced", "Fluent"],
                                key="r_isl_level")
            else:
                r_isl_exp, r_isl_level = 0, None

        # ── Bio ───────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">📝 Short Bio (Optional)</div>', unsafe_allow_html=True)
        r_bio = st.text_area("Tell us a little about yourself",
                             placeholder="I am a teacher who works with the deaf community…",
                             max_chars=300, height=90, key="r_bio")
        bio_cls = "char-ok" if 10 <= len(r_bio) <= 300 else ("char-bad" if len(r_bio) > 300 else "")
        st.markdown(f'<div class="char-count {bio_cls}">{len(r_bio)}/300</div>',
                    unsafe_allow_html=True)

        # ── Terms & progress ──────────────────────────────────────────────────
        st.markdown("<hr class='styled'>", unsafe_allow_html=True)
        r_agree = st.checkbox("I agree to the Terms & Conditions and Privacy Policy *",
                              key="r_agree")

        score = completion_score({
            "name": r_name, "dob": r_dob, "gender": r_gender,
            "phone": r_phone, "email": r_email,
            "language": r_language, "ISLSpeaker": r_isl,
        })
        st.markdown(progress_html(score), unsafe_allow_html=True)

        reg_submit = st.form_submit_button("🚀  Create Profile")

    # ── Validation & success ──────────────────────────────────────────────────
    if reg_submit:
        errors = []
        if not is_valid_name(r_name):          errors.append("Name must be at least 2 characters.")
        if not r_dob:                          errors.append("Please provide your Date of Birth.")
        if not is_valid_phone(r_phone):        errors.append("Phone number must be exactly 10 digits.")
        if not is_valid_email(r_email):        errors.append("Please enter a valid email address.")
        if len(r_password) < 6:                errors.append("Password must be at least 6 characters.")
        if r_password != r_password2:          errors.append("Passwords do not match.")
        if not r_agree:                        errors.append("You must accept the Terms & Conditions.")

        if errors:
            for err in errors:
                st.error(f"⚠️ {err}")
        else:
            # ── Check if email exists ──
            cursor.execute("SELECT email FROM users WHERE email = ?", (r_email,))
            if cursor.fetchone():
                st.error("⚠️ Email is already registered. Please log in.")
            else:
                # ── Store in database ──
                hashed_pw = hash_password(r_password)
                cursor.execute('''
                    INSERT INTO users (email, password, name, gender, dob, phone, language, notif, isl_speaker, isl_exp, isl_level, bio)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (r_email, hashed_pw, r_name.strip(), r_gender, str(r_dob), r_phone, r_language, r_notif, r_isl, r_isl_exp, r_isl_level, r_bio))
                conn.commit()
                
                st.session_state["logged_in"]  = True
                st.session_state["user_email"] = r_email
                st.session_state["user_name"]  = r_name.strip()

                st.success("🎉 Profile created successfully! You are now logged in.")
                st.balloons()

                # Confirmation card
                fields = {
                    "Full Name":          r_name,
                    "Date of Birth":      r_dob.strftime("%d %B %Y") if r_dob else "—",
                    "Gender":             r_gender,
                    "Phone":              f"+91 {r_phone}",
                    "Email":              r_email,
                    "Preferred Language": r_language,
                    "Notifications":      r_notif,
                    "ISL Speaker":        r_isl,
                }
                if r_isl == "Yes":
                    fields["ISL Experience"] = f"{r_isl_exp} year(s)"
                    fields["Proficiency"]    = r_isl_level
                if r_bio.strip():
                    fields["Bio"] = r_bio.strip()

                rows = "".join(
                    f'<div class="confirm-row">'
                    f'<span class="confirm-key">{k}</span>'
                    f'<span class="confirm-val">{v}</span>'
                    f'</div>'
                    for k, v in fields.items()
                )
                st.markdown(f"""
                <div style="margin-top:1rem;">
                    <strong style="color:#FF8C94;">✅ Registered Profile</strong>
                </div>
                <div class="confirm-card">{rows}</div>
                """, unsafe_allow_html=True)

                col_btn, _ = st.columns([1, 2])
                with col_btn:
                    if st.button("🚀  Go to Translator"):
                        st.switch_page("pages/main.py")