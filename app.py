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

background:#020617;

}


h1{

color:#38bdf8;

text-align:center;

}


button{

background:#06b6d4!important;

color:white!important;

}

</style>

""",
unsafe_allow_html=True
)



st.title("📚 Study Tutor AI")


question = st.text_area(
"Ask your question"
)



if st.button("Ask Tutor"):


    if question:


        with st.spinner(
            "Thinking..."
        ):


            answer = ask_tutor(

                question,

                get_memory()

            )


            save_memory(

                question,

                answer

            )


        st.success(answer)


    else:

        st.warning(
            "Enter a question"
        )
