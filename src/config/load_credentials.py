import streamlit as st

def load_credentials():
    username = st.secrets["credentials"]["username"]
    password = st.secrets["credentials"]["password"]
    return username, password