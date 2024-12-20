import streamlit as st
from config.load_credentials import load_credentials

def authenticate():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username, password = load_credentials()

        st.header("Login")
        input_username = st.text_input("Username")
        input_password = st.text_input("Password", type="password")

        if st.button("Login"):
            if input_username == username and input_password == password:
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.rerun()  # Force a rerun to update the UI
            else:
                st.error("Invalid username or password")

    return st.session_state.authenticated