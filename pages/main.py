import streamlit as st
from hemant import MTrans
from indicnlp.tokenize.sentence_tokenize import sentence_split
from sentence_to_gloss import SentenceToGloss
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

lexicon = {
    # Pronouns & indexing
    "i": "IX-1",
    "me": "IX-1",
    "my": "IX-1-POSS",
    "you": "IX-2",
    "your": "IX-2-POSS",
    "he": "IX-3M",
    "she": "IX-3F",
    "we": "IX-1PL",
    "they": "IX-3PL",
    "this": "THIS",
    "that": "THAT",
    "who": "WHO",
    "whose": "WHO-POSS",

    # Greetings & common
    "hello": "HELLO",
    "hi": "HELLO",
    "thank": "THANK-YOU",
    "thanks": "THANK-YOU",
    "sorry": "SORRY",
    "ok": "OK",
    "please": "PLEASE",
    "listen": "LISTEN",
    "look": "LOOK",
    "wait": "WAIT",
    "come": "COME",
    "go": "GO",
    "meet": "MEET",
    "later": "LATER",
    "now": "NOW",

    # Verbs
    "know": "KNOW",
    "help": "HELP",
    "talk": "TALK",
    "say": "SAY",
    "tell": "TELL",
    "call": "CALL",
    "eat": "EAT",
    "drink": "DRINK",
    "sleep": "SLEEP",
    "wake": "WAKE-UP",
    "work": "WORK",
    "rest": "REST",
    "reach": "REACH",
    "stop": "STOP",
    "turn": "TURN",
    "close": "CLOSE",
    "open": "OPEN",
    "charge": "CHARGE",

    # Time
    "today": "TODAY",
    "tomorrow": "TOMORROW",
    "yesterday": "YESTERDAY",
    "monday": "MONDAY",
    "minute": "MINUTE",
    "time": "TIME",
    "early": "EARLY",
    "late": "LATE",
    "fast": "FAST",
    "everyday": "EVERYDAY",

    # Places
    "home": "HOME",
    "office": "OFFICE",
    "school": "SCHOOL",
    "hospital": "HOSPITAL",
    "market": "MARKET",
    "station": "STATION",
    "outside": "OUTSIDE",
    "here": "HERE",
    "there": "THERE",

    # Family & people
    "friend": "FRIEND",
    "father": "FATHER",
    "mother": "MOTHER",
    "brother": "BROTHER",
    "sister": "SISTER",
    "child": "CHILD",
    "grandmother": "GRANDMOTHER",
    "people": "PEOPLE",

    # Food & drink
    "food": "FOOD",
    "water": "WATER",
    "tea": "TEA",
    "coffee": "COFFEE",
    "hungry": "HUNGRY",
    "thirsty": "THIRSTY",
    "sweet": "SWEET",
    "spicy": "SPICY",
    "salt": "SALT",
    "more": "MORE",
    "enough": "ENOUGH",

    # Shopping & money
    "money": "MONEY",
    "price": "PRICE",
    "expensive": "EXPENSIVE",
    "cheap": "CHEAP",
    "cash": "CASH",
    "receipt": "RECEIPT",
    "change": "CHANGE",
    "pack": "PACK",
    "kilo": "KILO",

    # Health
    "pain": "PAIN",
    "head": "HEAD",
    "fever": "FEVER",
    "cough": "COUGH",
    "dizzy": "DIZZY",
    "medicine": "MEDICINE",
    "doctor": "DOCTOR",
    "ambulance": "AMBULANCE",
    "injury": "INJURY",
    "blood": "BLOOD",
    "bandage": "BANDAGE",

    # Emotions & states
    "happy": "HAPPY",
    "sad": "SAD",
    "angry": "ANGRY",
    "fear": "FEAR",
    "worried": "WORRY",
    "tired": "TIRED",
    "sleepy": "SLEEPY",
    "busy": "BUSY",
    "free": "FREE",
    "bored": "BORED",
    "excited": "EXCITED",
    "shy": "SHY",
    "lonely": "LONELY",
    "relax": "RELAX",

    # Modifiers
    "not": "NOT",
    "very": "VERY",
    "all": "ALL"
}


glossifier = SentenceToGloss(
    nlp_model="en_core_web_sm",
    lexicon=lexicon
)

# functions
def hindi_to_english(text):
    sentences = sentence_split(text, "hi")
    translations = MTrans.mtrans("hi", "en", sentences)
    return translations

def english_to_gloss(sentences):
    gloss_output = []
    for s in sentences:
        gloss = glossifier.gloss_sentence(s)
        gloss_output.append(gloss)
    return gloss_output

# UI configuration
st.set_page_config(
    layout="wide",
    page_title="ISL System (Hindi → Gloss)",
    page_icon="🤖"
)

from utils.style import load_css
from utils.transition import page_transition

page_transition("fade")
load_css() 

st.title("ISL System – Hindi → English → Gloss")

if "english" not in st.session_state:
    st.session_state.english = ""

if "gloss" not in st.session_state:
    st.session_state.gloss = ""

col1, col2, col3 = st.columns(3)

# Input
with col1:
    st.subheader("Hindi Input")
    hindi_text = st.text_area(
        "Enter Hindi text",
        height=300
    )

    if st.button("Convert to Gloss"):
        if hindi_text.strip() == "":
            st.warning("Please enter Hindi text.")
        else:
            eng = hindi_to_english(hindi_text)
            st.session_state.english = "\n".join(eng)

            gloss = english_to_gloss(eng)
            st.session_state.gloss = "\n".join(gloss)

# English output
with col2:
    st.subheader("English Translation")
    st.text_area(
        "English",
        value=st.session_state.english,
        height=300,
        disabled=True
    )

# Gloss output
with col3:
    st.subheader("ISL Gloss Output")
    st.text_area(
        "Gloss",
        value=st.session_state.gloss,
        height=300,
        disabled=True
    )
