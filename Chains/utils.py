from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from pydantic import SecretStr
import os

load_dotenv()



class ChatModel:
    def __init__(self):
        try:
            api_key = os.environ.get("GROQ_API_KEY")
            self.chat = ChatGroq(
                api_key = SecretStr(api_key) if api_key else None,
                model ="gemma2-9b-it",
                temperature=0.7,
                max_tokens=512,
            )
        except Exception as e:
            print(f"An error occurred while initializing the chat model: {e}")
            self.chat = None    

    def retrive(self, messages):
        try:
            if not self.chat:
                return "Chat model not initialized properly."
            response = self.chat.invoke(messages)
            return response.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I encountered an error processing your request."