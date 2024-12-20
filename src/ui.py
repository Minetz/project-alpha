import streamlit as st

def show_audio(audio_bytes):
    if audio_bytes:
        st.audio(audio_bytes, format="audio/mp4")

def show_transcript(text):
    st.text_area("Trascrizione", value=text, height=400)

def display_conversation(response_text: str):
    st.write("## Conversazione")
    lines = response_text.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("<terapeuta>"):
            user_message = line.replace("<terapeuta>", "").strip()
            with st.chat_message("terapeuta"):
                st.write(user_message)
        elif line.startswith("<paziente>"):
            assistant_message = line.replace("<paziente>", "").strip()
            with st.chat_message("paziente"):
                st.write(assistant_message)
        else:
            # Handle lines without persona tags if needed
            pass