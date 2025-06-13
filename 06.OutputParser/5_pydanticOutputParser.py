from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the Model
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Make a pydantic Object 
class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt=18,description='Age of the person')
    city : str = Field(description='Name of the city the person belongs to')

# make a perser
parser = PydanticOutputParser(pydantic_object=Person)

# template
template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt
# prompt = template.invoke({'place':'indian'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result)

# We can make a chains insted of this 

chain = template | model | parser
final_result = chain.invoke({'place':'sri lankan'})
print(final_result)