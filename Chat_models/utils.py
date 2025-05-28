from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
import os

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

class ChatModel:
    def __init__(self):
        try:
            self.chat = ChatGroq(
                groq_api_key=os.getenv("GROQ_API_KEY"),
                model_name="gemma2-9b-it"
            )
        except Exception as e:
            print(f"An error occurred while initializing the chat model: {e}")
            self.chat = None    

    def retrive(self, messages: list):
        try:
            if not self.chat:
                return "Chat model not initialized properly."
            response = self.chat.invoke(messages)
            return response.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I encountered an error processing your request."