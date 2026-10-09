import streamlit as st


from agent import ask_tutor

from memory import save_memory



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

color:#94a3b8;

text-align:center;

font-size:18px;

}



.stButton button{


background:#06b6d4;

color:white;

border-radius:12px;

height:45px;

width:150px;


}



textarea{

border-radius:15px;

}


</style>

""",

unsafe_allow_html=True
)




st.title("📚 Study Tutor Agent")


st.markdown(

"""
<div class="subtitle">

Your AI powered learning companion 🚀

</div>

""",

unsafe_allow_html=True

)



question=st.text_area(

"Ask your study question:",

height=120

)



if st.button("Ask Tutor"):


    if question:


        with st.spinner(
            "Tutor is thinking..."
        ):


            answer=ask_tutor(question)


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



st.divider()


st.caption(

"Built with CrewAI + Groq + Streamlit"

)
