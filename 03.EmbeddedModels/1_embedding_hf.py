import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# convert this document in embeddings 
documents = ['Delhi is the capital of India',
             'Kolkata is the capital of West Bengal',
             'Paris is the capital of France'
             ]

# Store it in variable 
vector = embedding.embed_documents(documents) # Multiple list documents 
print(str(vector))
