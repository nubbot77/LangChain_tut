from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# template = "Tell me all research papers about {topic} in {language} language."

# prompt_template = ChatPromptTemplate.from_template(template=template)

# print("__________Prompt from Template__________")

# prompt = prompt_template.invoke({'topic':'transformers','language':'English'})

# print(prompt)



# We cant use SystemMessage or HummanMessage directly in the message. If we want to insert values in SystemMessage or HumanMessage. Instead we can use a list of tuples with the first element as the type of message and the second element as the content of the message.


messages = [
    ('system', 'You are a helpfull assistant.'),
    ('human', 'Tell me all research papers about {topic} in {language} language.')
]

prompt_temp = ChatPromptTemplate.from_messages(messages = messages)

print("__________Prompt from messages__________")
prompt = prompt_temp.invoke({'topic':'transformers','language':'English'})
print(prompt)