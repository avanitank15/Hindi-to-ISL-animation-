import streamlit as st
from utils.style import load_css
from utils.transition import page_transition

page_transition("fade")
load_css()

st.title("User Login Form")

# Initialize session state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

form_values = {
    "name": None,
    "age": None,
    "gender": None,
    "ISLSpeaker": None
}

with st.form(key="userInfoForm"):
    form_values["name"] = st.text_input("Enter your name")
    form_values["age"] = st.number_input("Enter your age", step=1)
    form_values["gender"] = st.radio("Gender", ["Male", "Female"])
    form_values["ISLSpeaker"] = st.radio("Have you learned ISL?", ["YES", "NO"])

    submit_button = st.form_submit_button("Login")

    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill all the fields")
        else:
            st.session_state.form_submitted = True
            st.balloons()

# ---- AFTER FORM ----
if st.session_state.form_submitted:
    st.write("### Please confirm your information")
    for key, value in form_values.items():
        st.write(f"**{key}** : {value}")

    st.divider()

    if st.button("⬅ Back to Home"):
        st.switch_page("pages/home.py")
