
import streamlit as st
from hemant import MTrans
from indicnlp.tokenize.sentence_tokenize import sentence_split
from sentence_to_gloss import SentenceToGloss
import os
import speech_recognition as sr
from moviepy import VideoFileClip, concatenate_videoclips
import base64

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

lexicon = {
    # Pronouns & indexing
    "i": "I",
    "me": "I",
    "my": "I",
    "you": "YOU",
    "your": "YOU",
    "he": "HE",
    "she": "HE",
    "we": "WE",
    "they": "THEY",
    "this": "THIS",
    "that": "THAT",
    "who": "WHO",
    "whose": "WHOSE",
    "how":"HOW",
    "we":"WE",
    "yes":"YES",
    "no":"NO",
    "not":"NO",

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
    "want":"WANT",

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
    "tuesday": "TUESDAY",
    "wednesday": "WEDNESDAY",
    "thursday": "THURSDAY",
    "friday": "FRIDAY",
    "saturday": "SATDAY",
    "sunday": "SUNDAY",
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
    "friends": "FRIEND",
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

def voice_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 बोलिए... (Speak now)")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech service error"

def merge_videos(words, video_dir):
    clips = []

    for word in words:
        word = word.strip().lower()

        for file in os.listdir(video_dir):
            clean_name = file.lower().replace(".mp4", "")

            if clean_name == word:
                path = os.path.join(video_dir, file)
                clips.append(VideoFileClip(path))
                break

    if not clips:
        return None

    final_clip = concatenate_videoclips(clips, method="compose")

    output_path = os.path.join(video_dir, "output.mp4")
    final_clip.write_videofile(output_path, codec="libx264", audio=False)

    return output_path

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

st.title("Hindi to ISL Translation System")

if "english" not in st.session_state:
    st.session_state.english = ""

if "gloss" not in st.session_state:
    st.session_state.gloss = ""

col1,col2, col3 = st.columns(3)
       
            

# Input
with col1:
    
    hindi_text = st.text_area(
        "Enter Hindi text",
        height=300
    )

    # 🎤 Voice + Convert
    if st.button("🎤 Speak & Convert"):
        spoken_text = voice_to_text()
        st.success(f"Recognized: {spoken_text}")

        eng = hindi_to_english(spoken_text)
        st.session_state.english = "\n".join(eng)

        gloss = english_to_gloss(eng)
        st.session_state.gloss = "\n".join(gloss)

        # 📝 Manual Convert
    if st.button("Convert to Gloss"):
        if hindi_text.strip() == "":
            st.warning("Please enter Hindi text.")
        else:
            eng = hindi_to_english(hindi_text)
            st.session_state.english = "\n".join(eng)

            gloss = english_to_gloss(eng)
            st.session_state.gloss = "\n".join(gloss)


# Gloss output
with col2:
    st.text_area(
        "Gloss",
        value=st.session_state.gloss,
        height=300,
        disabled=True
    )


#Find Video
def find_video(word, video_dir):
    word = word.strip().lower()

    for file in os.listdir(video_dir):
        clean_file = file.lower().replace(".mp4", "").strip()

        if clean_file == word:
            return os.path.join(video_dir, file)

    return None

#  output
with col3:
    # st.text_area(
    #     "Gloss",
    #     value=st.session_state.gloss,
    #     height=300,
    #     disabled=True
    # )
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # → pages/
    ROOT_DIR = os.path.dirname(BASE_DIR)                    # → project root
    VIDEO_DIR = os.path.join(ROOT_DIR, "signs_zip")         # → signs_zip/
    if st.session_state.gloss:
        sentences = st.session_state.gloss.split("\n")

        for sentence in sentences:
            words = sentence.split()

            final_video = merge_videos(words, VIDEO_DIR)

            # if final_video:
            #     st.video(final_video, autoplay=True)
            # else:
            #     st.error("No videos found ❌")
            if final_video:
                with open(final_video, "rb") as f:
                    video_bytes = f.read()
                    encoded = base64.b64encode(video_bytes).decode()
                st.markdown(
                    f"""
                    <video width="100%" height="300" controls autoplay>
                        <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
                    </video>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error("No videos found ❌")
