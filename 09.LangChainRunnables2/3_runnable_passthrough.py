from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGroq(
    model_name='llama3-8b-8192',
    temperature=0,
    streaming=False
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variables=['text']
)

# Form a Chain Joke generator Chain
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# Parallel Chain
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

# Connect all the chains 
# Final Chain
final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic','cricket'}))