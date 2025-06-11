from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(models='gpt-4',temperature=0,max_complietion_tokens=10) 
result = model.invoke("What is the capital of India?")
print(result) # get asnwer and metadata as well
print(result.content) # to get the answer 