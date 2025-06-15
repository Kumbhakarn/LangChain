from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gep-3.5-turbo-instruct")
result = llm.invoke("What is the capital of India") # we can communicate with the mode 
print(result)

# LLMs are older and not used in current 
# we use Chat Models as they are new and with more advance useage