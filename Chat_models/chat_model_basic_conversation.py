from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
import os
from utils import ChatModel

model = ChatModel()


# The SystemMessage is used to "prime" or instruct the AI on how to behave.
# The HumanMessage (when spelled correctly) represents input from the user.
# The AIMessage represents a response from the AI model, typically used to store or simulate previous AI replies in a conversation history.
# The SystemMessage is used to instruct or guide the AI's behavior, setting context or rules for the conversation.

message = [
    SystemMessage(content="You are a helpfull assistant"),
    HumanMessage(content="What is capital of kerala?"),
]
result = model.invoke(message)

# print("Full result:\n",result)
print("_______________XXXXXXXX_____________")
print("Content only:\n",result.content)
print("_______________XXXXXXXX_____________")