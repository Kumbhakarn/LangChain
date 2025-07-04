from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()  

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task='text-generation'  
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")
print(response.content) 