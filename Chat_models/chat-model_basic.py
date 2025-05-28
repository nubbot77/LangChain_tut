from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from utils import ChatModel

model = ChatModel()

result = model.retrive("What is capital of kerala?")

print("Full result:\n",result)
print("_______________XXXXXXXX_____________")
print("Content only:\n",result.content)
print("_______________XXXXXXXX_____________")