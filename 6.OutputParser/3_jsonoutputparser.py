from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

## JSON output parser
parser = JsonOutputParser()

# Write a prompt with the help of promptTemplate
template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions}
)

# make a Prompt
# prompt = template.format()
# # print(prompt) 

# result = model.invoke(prompt)
# # print(result)

# # parse the result withe the help of parser method
# final_result = parser.parse(result.content)

# Output in JSON format
# print(final_result)
# print(final_result['name'])
# print(type(final_result))


# We can make Chains insted of above three lies of code
# It is a easier way and we are usning thins in going forward
chain  = template | model | parser
result = chain.invoke({}) # if we dont have any input_variable we have to send 
# the blank dictionary in chain.invoke
print(result)

