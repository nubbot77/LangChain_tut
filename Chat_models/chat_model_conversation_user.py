from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
import os
from utils import ChatModel


model = ChatModel()
chat_history = []

system_message = SystemMessage(content="You are a helpful AI assistant. Answer the questions to the best of your abilities. Don't give wrong information. If you don't know the answer, say you don't know.")
chat_history.append(system_message)

while True:
    query = input("Enter your Query: ")
    if query.lower() == "exit":
        break
    
    human_message = HumanMessage(content=query)
    chat_history.append(human_message)

    response = model.retrive(chat_history)
    print("AI Response:", response)
    chat_history.append(AIMessage(content=response))