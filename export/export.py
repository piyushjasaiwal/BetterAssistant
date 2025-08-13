import time
import re
import os
from langchain_core.messages import HumanMessage, AIMessage

def export(filename = "logs", chat = []):
    timestamp = int(time.time())
    os.makedirs("logs", exist_ok=True)

    filename = re.sub(r"\..*$", "", filename)
    filename = f"logs/{filename}_{timestamp}.txt"

    with open(file=filename, mode="w") as file:
        file.write("<==================================Conversation Log:==================================>\n\n")

        for message in chat:
            if isinstance(message, HumanMessage):
                file.write(f"User: {message.content[0]['query']}\n") # type: ignore
            elif isinstance(message, AIMessage):
                file.write(f"Bot: {message.content[0]['response']}\n\n") # type: ignore

        file.write("<===================================End of Conversation================================>\n")

    print(f"Conversation saved to {filename}")
