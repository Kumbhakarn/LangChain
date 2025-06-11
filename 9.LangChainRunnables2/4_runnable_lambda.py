from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()


# Write a function to pass for runnable lambda
def word_count(text):
    return len(text.split())


# PromptTemplate
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

# Model
model = ChatGroq(
    model_name = "llama3-8b-8192",
    temperature=0.5,
    streaming=False
)

# OutputParser
parser = StrOutputParser()

# Form a Chain RunnableSequence
# joke_gen_chain = RunnableSequence(prompt, model, parser)

# ----------LCEL--------------------------------
# LCEL New way to define RunnableSequence Chains
joke_gen_chain = prompt | model | parser

# Parallel Chain
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
    # 'word_count':RunnableLambda(lambda x: len(x.split())) # Another way to exicute the RunnableLambda
})

# FinalChain
# final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# -----------------------LCEL-----------------------------LangChain Expression Language
final_chain = joke_gen_chain | parallel_chain
# invoke the chain
result = final_chain.invoke({'topic':'AI'})

final_result = """ {} \n word count - {}""".format(result['joke'],result['word_count'])
print(final_result)
