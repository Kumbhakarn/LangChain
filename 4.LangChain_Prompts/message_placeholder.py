from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

# chat template

chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

# load chat history

# safely load chat history
file_path = r'chat_history.txt'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        chat_history.extend(f.readlines())
else:
    print(f" File '{file_path}' not found. Proceeding with empty chat history.")

print(chat_history)

# create prompt

prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
print(prompt)