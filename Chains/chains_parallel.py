from utils import ChatModel
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda,RunnableParallel


model = ChatModel()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a expert product reviewer.'),
        ('human', 'List the main features of product {product_name}')
    ]
)

def analyze_pros(features):
    pros_temp = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are a expert product reviewer.'),
            ('human', 'Given these features: {features}, list the pros of the product.'),
        ]
    )
    return pros_temp.format_messages(features=features)

def analyze_cons(features):
    cons_temp = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are a expert product reviewer.'),
            ('human', 'Given these features: {features}, list the cons of the product.'),
        ]
    )
    return cons_temp.format_messages(features=features)

def combine_results(pros,cons):
    return f"Pros: {pros}\nCons: {cons}"

pros_branch_chain = RunnableLambda(lambda x: analyze_pros(x)) |model.retrive | StrOutputParser()

cons_branch_chain = RunnableLambda(lambda x: analyze_cons(x)) | model.retrive | StrOutputParser()


print_feature = RunnableLambda(lambda x: print(f"Product Features: {x}\n\n "))

chain = prompt_template | model.retrive | StrOutputParser() | print_feature | RunnableParallel(branches={"pros": pros_branch_chain, "cons":cons_branch_chain})| RunnableLambda(lambda x:combine_results(x['branches']['pros'], x['branches']['cons'])) # type: ignore


result = chain.invoke({'product_name': 'Samsung Galaxy S25 Ultra'})

print(result)
    