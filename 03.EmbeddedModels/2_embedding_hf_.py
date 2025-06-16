from langchain_huggingface import HuggingFaceEmbeddings

# Importing Model using HuggingFace
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
text = 'Delhi is the capital of India'

# Store it in variable
vector = embedding.embed_query(text)
print(str(vector))