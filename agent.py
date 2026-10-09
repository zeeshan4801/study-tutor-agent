from crewai import Agent, Task, Crew

from groq import Groq

from config import get_api_key

from tools import CalculatorTool



client = Groq(
    api_key=get_api_key()
)



class GroqLLM:


    def call(self, prompt):

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        )


        return response.choices[0].message.content





llm = GroqLLM()



calculator = CalculatorTool()



def create_agent():


    tutor = Agent(

        role="Study Tutor",

        goal="""
        Teach students clearly.
        Explain concepts,
        create quizzes,
        and make study plans.
        """,

        backstory="""
        You are a patient professional teacher.
        Always explain in simple words.
        """,

        llm=llm,

        tools=[calculator],

        verbose=False

    )


    return tutor





def ask_tutor(question, memory):


    tutor=create_agent()


    task=Task(

        description=f"""

        Student question:

        {question}


        Previous memory:

        {memory}


        Give:

        - Simple explanation
        - Examples
        - Summary

        """,

        expected_output="""

        Educational answer

        """,

        agent=tutor

    )


    crew=Crew(

        agents=[tutor],

        tasks=[task]

    )


    result=crew.kickoff()


    return str(result)
