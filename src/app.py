import streamlit as st
from config.auth import authenticate
from openai_client import get_client
from transcription import transcribe_audio
from gpt_prompt import repair_transcription
from ui import show_audio, show_transcript, display_conversation

st.set_page_config(layout="wide")

# Initialize session states
if 'audio_bytes' not in st.session_state:
    st.session_state.audio_bytes = None
if 'transcription' not in st.session_state:
    st.session_state.transcription = None
if 'gpt_response' not in st.session_state:
    st.session_state.gpt_response = None


# First, run authentication logic
authenticated = authenticate()

# Check authentication
if authenticated:
    # If authenticated, show the rest of your application

    client = get_client()

    st.title("OCDCompass: Transcrizione di conversazione con Ai")

    # Step 1: Load audio file
    st.header("Caricare il file audio:")
    audio_file = st.file_uploader("Upload audio (.mp3, .m4a)", type=["mp3", "m4a"])
    if audio_file is not None:
        st.session_state.audio_bytes = audio_file.read()

    st.header("Utilizzare un file audio di esempio")
    if st.button("Usa file audio di esempio"):
        with open("data/sample_audio.m4a", "rb") as f:
            st.session_state.audio_bytes = f.read()

    # Always show audio preview if available
    show_audio(st.session_state.audio_bytes)

    # Process audio with Whisper
    if st.button("Processa Audio seduta psicologica"):
        if not st.session_state.audio_bytes:
            st.error("Caricare file audio")
        else:
            transcription = transcribe_audio(client, st.session_state.audio_bytes)
            st.session_state.transcription = transcription
            st.success("Trascrizione completata")

    # Always show transcription if available
    if st.session_state.transcription is not None:
        show_transcript(st.session_state.transcription.text)


    # Prompt GPT-4o with transcription
    if st.button("Pro mode: Ripara trascrizione"):
        if not st.session_state.transcription:
            st.error("Prima devi trascrivere l'audio")
        else:
            
            gpt_response = repair_transcription(client, st.session_state.transcription.text)
            st.session_state.gpt_response = gpt_response

    # Always show GPT response if available
    if st.session_state.gpt_response is not None:
        #st.text_area("Trascrizione pro", value=st.session_state.gpt_response, height=400)
        display_conversation(st.session_state.gpt_response)
