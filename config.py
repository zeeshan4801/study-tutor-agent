import streamlit as st


def get_groq_key():

    try:
        return st.secrets["GROQ_API_KEY"]

    except Exception:

        raise Exception(
            "GROQ_API_KEY missing. Add it in Streamlit Secrets."
        )
