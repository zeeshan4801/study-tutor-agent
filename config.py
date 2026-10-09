import streamlit as st


def get_groq_key():

    return st.secrets["GROQ_API_KEY"]
