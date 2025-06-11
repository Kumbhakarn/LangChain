from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# Prompt  Runnable1 (Runnable-TaskSpecific)
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

# Model  Runnable2 (Runnable-TaskSpecific)
model = ChatGroq(
    model_name='llama3-8b-8192',
    temperature=0,
    streaming=False
)

# Output_Parser Runnable3 (Runnable-TaskSpecific)
parser = StrOutputParser()

# Prompt2 (Runnable-TaskSpecific)
prompt2 = PromptTemplate(
    template="Explain the fallowing joik - {text}",
    input_variables=['text']
)

# Chain  SiquentialChain built using ---> RunnableSequence (RunnablePrimitive)
# Combining Multiple workflows using runnable
# chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# -------------------LCEL----------------------
# New Way to define RunnableSequence chains by using pip operator =  | 
chain = prompt1 | model | parser | prompt2 | model | parser
# invoke the chain
print(chain.invoke({'topic':'AI'}))
