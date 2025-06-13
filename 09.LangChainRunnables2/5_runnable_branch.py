from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableParallel, RunnableLambda,RunnablePassthrough, RunnableSequence
from dotenv import load_dotenv
load_dotenv()


# prompt1 
prompt1 = PromptTemplate(
    template='Writea a detail report on {topic}',
    input_variables=['topic']
)
# prompt2
prompt2 = PromptTemplate(
    template="Summarize the fallowing text \n {topic}",
    input_variables=['text']
)

# Model
model = ChatGroq(
    model_name='llama3-8b-8192',
    temperature=0.7,
    streaming=False
)

# OutputParser
parser = StrOutputParser()

# Report Generation Chain 
# report_gen_chain = RunnableSequence(prompt1,model,parser)

# New Way to Define RunnableSequence Chains using LCEL
# LangChain Expression Language
report_gen_chain = prompt1 | model | parser

# branch Chain
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

# Final Chain
# final_chain = RunnableSequence(report_gen_chain,branch_chain)

# Chain using LCEL # LangChain Expression Language New way to define RunnableSequence chains
final_chain = report_gen_chain | branch_chain

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))