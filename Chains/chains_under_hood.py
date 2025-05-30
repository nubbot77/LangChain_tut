from utils import ChatModel
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda


model = ChatModel()

prompt_temp = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpfull assistant.'),
        ('human', 'Name some of the most popular frameworks of a {programming_lang} programming language.'),
    ]
)

format_prompt = RunnableLambda(lambda x: prompt_temp.format_messages(**x))
invoke_model = RunnableLambda(lambda x: model.retrive(x))
parse_output = StrOutputParser()


chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

response = chain.invoke({'programming_lang': 'Python'})
print(response)

