# from langchain.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
# from langchain.llms import openai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load the document 
loader = TextLoader(r'E:/15_CampusX_LangChain/8.LangChainRunnables/docs.txt')
documents = loader.load()

# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# convert text into embeddings and store in FAISS
vectorstore = FAISS.from_documents(docs,HuggingFaceEmbeddings())

# create a retriever (fetch relevant documents)
retriever = vectorstore.as_retriever()

# Manually Retrieve Relevant Documents
query = 'What are the key takeways from the documents?'
retriever_docs = retriever.get_relevant_documents(query)

# Combine Retrieved Text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retriever_docs])

# Initialize the LLM
# Define the Model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Manually Pass Retrueved Text to LLM
prompt = f"Based on the fallowing text, answer the questions: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

# Print the answer
print("Answer: ",answer)
