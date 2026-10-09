import streamlit as st

from agent import ask_tutor


st.set_page_config(

    page_title="Study Tutor AI",

    page_icon="📚",

    layout="centered"

)


st.markdown(
"""
<style>

body{

background:#020617;

}


.main{

background:#020617;

}


h1{

color:#38bdf8;

}


.stButton button{

background:#0ea5e9;

color:white;

border-radius:10px;

}

</style>

""",

unsafe_allow_html=True
)



st.title("📚 Study Tutor Agent")

st.subheader(
"Your AI powered learning companion"
)



question=st.text_area(

"Ask your tutor anything"

)



if st.button("Ask Tutor"):


    if question:


        with st.spinner("Thinking..."):

            answer=ask_tutor(question)


        st.success(answer)

    else:

        st.warning(
        "Please enter a question"
        )
