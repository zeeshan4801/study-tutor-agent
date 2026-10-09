import os

from crewai import Agent, Task, Crew, Process
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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



def create_tutor_agent():

    tutor = Agent(

        role="AI Study Tutor",

        goal="""
        Help students learn concepts,
        create study plans,
        generate quizzes,
        and explain difficult topics.
        """,

        backstory="""
        You are a patient teacher.
        You explain everything in simple language.
        You use examples and practical explanations.
        """,

        llm=llm

    )


    return tutor



def ask_tutor(question):

    tutor=create_tutor_agent()


    task=Task(

        description=question,

        expected_output="""
        A clear educational answer
        with examples and explanation.
        """,

        agent=tutor

    )


    crew=Crew(

        agents=[tutor],

        tasks=[task],

        process=Process.sequential

    )


    result=crew.kickoff()


    return result
