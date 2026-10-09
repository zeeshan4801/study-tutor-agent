from crewai import Agent, Task, Crew, LLM

from config import get_groq_key

from tools import CalculatorTool



API_KEY = get_groq_key()



llm = LLM(

    model="groq/openai/gpt-oss-120b",

    api_key=API_KEY,

    temperature=0.3

)



calculator = CalculatorTool()



def create_agent():

    tutor = Agent(

        role="AI Study Tutor",

        goal="""
        Help students learn difficult topics,
        create study plans,
        explain concepts,
        and generate quizzes.
        """,

        backstory="""
        You are a professional teacher.
        You explain everything step by step.
        You use simple examples.
        """,

        llm=llm,

        tools=[
            calculator
        ],

        verbose=True

    )


    return tutor





def ask_tutor(question, memory):


    tutor=create_agent()



    task=Task(

        description=f"""

        Student Question:

        {question}


        Previous Conversation:

        {memory}


        Give answer with:

        1. Simple explanation
        2. Examples
        3. Short summary


        """,

        expected_output="""

        Clear educational answer.

        """,

        agent=tutor

    )



    crew=Crew(

        agents=[
            tutor
        ],

        tasks=[
            task
        ]

    )



    result=crew.kickoff()



    return str(result)
