chat_memory = []


def save_memory(question, answer):

    chat_memory.append(
        {
            "question": question,
            "answer": answer
        }
    )



def get_memory():

    return chat_memory[-5:]
