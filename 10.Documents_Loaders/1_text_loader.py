from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

# call the model
model = ChatGroq(
    model_name='llama3-8b-8192',
    temperature=0.5,
    streaming=False
)

# promptTemplate
prompt = PromptTemplate(
    template='Write a summary for the fallowing speech- \n {speech}',
    input_variables=['speech']
)

# OutPutParser
parser = StrOutputParser()



file_path = '8.LangChainRunnables/speech.txt'
# Object loader
loader = TextLoader(file_path)
# Call the funcion loader.load to
docs = loader.load()


# we get a list of documents
# print(type(docs)) # python list
# print('*'*50)
# print("Number of Documents: ",len(docs))
# print('*'*50)
# print(docs[0])
# print('*'*50)
# print("Type of document: ",type(docs[0]))
# print('*'*50)
# print("Page Content: ",docs[0].page_content)
# print('*'*50)
# print("Metadaa: ",docs[0].metadata)

# Form a chain
chain = prompt | model | parser
# chain.invoke
print(chain.invoke({'speech':docs[0].page_content}))