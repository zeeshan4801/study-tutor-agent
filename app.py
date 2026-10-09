import streamlit as st


from agent import ask_tutor

from memory import save_memory,get_memory



st.set_page_config(

    page_title="Study Tutor AI",

    page_icon="📚"

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


.stButton button{

background:#06b6d4;
color:white;
border-radius:12px;

}

</style>

""",
unsafe_allow_html=True
)



st.title("📚 Study Tutor AI")


st.write(
"Your AI powered learning companion 🚀"
)



question = st.text_area(

    "Ask your question",

    height=120

)



if st.button("Ask Tutor"):


    if question:


        with st.spinner(
            "Tutor is thinking..."
        ):


            answer = ask_tutor(

                question,

                get_memory()

            )


            save_memory(

                question,

                answer

            )


        st.success("Answer")

        st.write(answer)



    else:

        st.warning(
            "Please enter a question"
        )
