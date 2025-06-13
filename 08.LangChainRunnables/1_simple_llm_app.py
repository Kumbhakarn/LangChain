from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


# Initialize the LLM

llm = OpenAI(model_name="gpt-3.5-turbo",temperature=0.7)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=['topic'],
    template="suggest a catchy blog title about {topic}."
)

# Define the input
topic = input('Enter a topic')

# format the prompt manually using prompttemplate
formatted_prompt = prompt.format(topic=topic)

# call the LLM directly
blog_title = llm.predict(formatted_prompt)

# print the output
print('Generated Blog Title: ',blog_title)
