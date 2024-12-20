import streamlit as st

def load_api_key():
    return st.secrets["openai"]["api_key"]