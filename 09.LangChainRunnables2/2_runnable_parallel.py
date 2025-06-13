from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
load_dotenv()


# Prompt1 Runnable-TaskSpecific 1
prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

# Prompt2 Runnable-TaskSpecific 2
prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=['topic']
)

# Model Runnable- TaskSpecific 3
model = ChatGroq(
    model_name = 'llama3-8b-8192',
    temperature=0,
    streaming=False
)

# OutPut Parser 
parser = StrOutputParser()

# Runnable Parallel
# paralleli exicuting two workflows 
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)