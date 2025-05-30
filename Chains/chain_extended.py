from utils import ChatModel
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda



model = ChatModel()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpfull assistant.'),
        ('human', '{question}')
    ]
)

print(prompt_template + "\n")

parse_output = StrOutputParser()

format_prompt = RunnableLambda(lambda x:
                               prompt_template.format_messages(**x))

uppercase_output = RunnableLambda(lambda x: str(x).upper())
count_words = RunnableLambda(lambda x: f"Word Count: {len(str(x).split())}\n{x}")


chain = format_prompt | model.retrive | parse_output | uppercase_output | count_words 


result = chain.invoke({'question': 'What is your age?'})
print(result)

print("\n")


