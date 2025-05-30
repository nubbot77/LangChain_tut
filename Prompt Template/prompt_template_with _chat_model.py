from utils import ChatModel
from langchain.prompts import ChatPromptTemplate


model = ChatModel()

print("-----prompt from template-----")
messages = [
    ('system', 'You are a helpfull assistant.'),
    ('human', 'Tell me summary of research paper {topic} in {language} language.')
]

prompt_temp = ChatPromptTemplate.from_messages(messages = messages)

print("__________Prompt from messages__________")
prompt = prompt_temp.invoke({'topic':'Attention All you need','language':'English'})
print(prompt)

res = model.retrive(prompt)
print(res)
