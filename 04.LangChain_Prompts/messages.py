from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


load_dotenv()
hf_token = os.getenv('HF_TOKEN')

llm = HuggingFaceEndpoint(repo_id = "meta-llama/Llama-3.1-8B-Instruct",
                        task="text-generation",
                        huggingfacehub_api_token = hf_token)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content=' ')
]

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)