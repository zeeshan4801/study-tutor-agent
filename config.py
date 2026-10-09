import streamlit as st


def get_api_key():

    try:
        return st.secrets["GROQ_API_KEY"]

    except Exception:

        raise Exception(
            "Please add GROQ_API_KEY in Streamlit Secrets"
        )
