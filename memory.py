memory = []


def save_memory(question, answer):

    memory.append(
        {
            "question": question,
            "answer": answer
        }
    )


def get_memory():

    return memory[-5:]
