# LLM Chain of simple_llm application 
# We are buinding components and making the process automate

from langchain.llms import OpeAI 
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

## Load the LLM (GPT-3.5)
llm = OpenAI(model_name='gpt-3.5-turbo',temperature=0.7)

# Create a Prompt Template

prompt = PromptTemplate(
    input_variables=["Topic"], # Defines what input is neede
    template="Suggest a catchy nlog title about {topic}."
)

# create an LLM Chain
chain = LLMChain(llm=llm,prompt=prompt)

# the chain with specific topic
topic = input("Enter a topic")
output = chain.run(topic)

print("Generated BLog Title: ",output)