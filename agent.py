from crewai import Agent, Task, Crew, LLM

from config import GROQ_API_KEY

from tools import CalculatorTool

from memory import get_memory



llm = LLM(

    model="groq/openai/gpt-oss-120b",

    api_key=GROQ_API_KEY,

    temperature=0.3

)



calculator = CalculatorTool()



def create_study_agent():


    agent = Agent(

        role="AI Study Tutor",

        goal="""
        Help students understand difficult concepts,
        create study plans, explain topics,
        and generate quizzes.
        """,

        backstory="""
        You are a friendly expert teacher.
        You explain concepts step by step.
        You use simple language,
        examples and practical explanations.
        """,

        llm=llm,

        tools=[calculator],

        verbose=False

    )


    return agent



def ask_tutor(question):


    agent=create_study_agent()


    previous = get_memory()


    context=""


    if previous:

        context=f"""
        Previous conversation:

        {previous}
        """



    task=Task(

        description=f"""

        {context}


        Student question:

        {question}


        Answer like a professional tutor.

        Include:
        - Simple explanation
        - Examples
        - Summary

        """,

        expected_output="""

        A clear educational answer.

        """,

        agent=agent

    )



    crew=Crew(

        agents=[agent],

        tasks=[task],

    )


    result=crew.kickoff()


    return str(result)
