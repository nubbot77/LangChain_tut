from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from utils import ChatModel 


model = ChatModel()


prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpfull assistant.'),
        ('human', '{question}')
    ]
)


# langchain Expression Language (LCEL) chain
chain = prompt_template | model.retrive | StrOutputParser()

result = chain.invoke({'question':'What is your age?'})

print(result)