from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # reusable library Most used componenets are here
from langchain_core.output_parsers import JsonOutputParser # reusable library
from langchain.output_parsers import StructuredOutputParser,ResponseSchema # core library

load_dotenv()

# Defined the model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

# make a schema with the help of Response Schema
schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

# Create a prompt template
template = PromptTemplate(
    template="Give 3 facts about the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# Write down the prompt
# prompt = template.invoke({'topic':'black hole'})
# give prompt to the model
# result = model.invoke(prompt)
# give the result to the parser
# final_result = parser.parse(result.content)
# print(final_result)

# Going forward we are using chains 

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)