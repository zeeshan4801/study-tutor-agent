import streamlit as st


from agent import ask_tutor

from memory import save_memory, get_memory



st.set_page_config(

    page_title="Study Tutor AI",

    page_icon="📚",

    layout="centered"

)



st.markdown(
"""
<style>

.stApp{

background:
linear-gradient(
135deg,
#020617,
#0f172a
);

}


h1{

color:#38bdf8;
text-align:center;

}


.subtitle{

text-align:center;
color:#94a3b8;
font-size:20px;

}


.stButton button{

background:#06b6d4;

color:white;

border-radius:15px;

font-size:18px;

height:45px;

width:160px;

}


</style>

""",
unsafe_allow_html=True
)



st.title(
"📚 Study Tutor Agent"
)


st.markdown(
"""
<div class="subtitle">

Your AI Learning Companion 🚀

</div>
""",
unsafe_allow_html=True
)



question = st.text_area(

    "Ask your tutor:",

    placeholder=
    "Example: Explain Newton's law in simple words",

    height=120

)



if st.button("Ask Tutor"):


    if question:


        with st.spinner(
            "AI Tutor is thinking..."
        ):


            memory=get_memory()


            answer=ask_tutor(
                question,
                memory
            )


            save_memory(
                question,
                answer
            )


        st.success("Answer")

        st.write(answer)



    else:

        st.warning(
            "Please enter a question."
        )



st.divider()


st.caption(
"Built with CrewAI + Groq + Streamlit"
)
