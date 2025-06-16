# Sample chatbot using HuggingFaceEndpoint

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage

load_dotenv()
hf_token = os.getenv('HF_TOKEN')

llm = HuggingFaceEndpoint(repo_id = "meta-llama/Llama-3.1-8B-Instruct",
                        task="text-generation",
                        huggingfacehub_api_token = hf_token)

model = ChatHuggingFace(llm=llm)

# User Chat History 
chat_history = [
    SystemMessage(content = 'Your are a helpful AI assistant')
 
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)

print(chat_history)