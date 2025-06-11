from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Prompt
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)
model = ChatOpenAI()
# parser
parser = StrOutputParser()
# Chains "Simple chain"
# | = pipe operator (LangChain Expression Language) LCEL 
chain = prompt | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)
# visualize your chain
chain.get_graph().print_ascii()


