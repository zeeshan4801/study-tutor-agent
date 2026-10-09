from groq import Groq

from config import get_groq_key

from tools import CalculatorTool



client = Groq(
    api_key=get_groq_key()
)



calculator = CalculatorTool()



class StudyTutorAgent:


    def run(self, question, history):


        prompt = f"""

You are an expert AI Study Tutor.

Student question:

{question}


Previous conversation:

{history}


Your job:

- Explain simply
- Give examples
- Add a short summary
- Help the student learn


"""


        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[

                {
                    "role":"system",
                    "content":
                    "You are a helpful study tutor."
                },

                {
                    "role":"user",
                    "content":prompt
                }

            ],

            temperature=0.3

        )


        return response.choices[0].message.content




def ask_tutor(question, memory):


    agent = StudyTutorAgent()


    answer = agent.run(

        question,

        memory

    )


    return answer
