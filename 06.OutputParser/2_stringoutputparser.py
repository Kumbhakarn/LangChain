# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from transformers import pipeline
from langchain_community import HuggingFacePipeline


load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2b-it",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# We are using opensour model from Huggingface Transformers
pipe = pipeline("text-generation",model="HuggingFaceH4/zephyr-7b-beta")
model = HuggingFacePipeline(pipeline=pipe)


# 1st prompt template --> Detailed Report

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

# 2nd prompt template -- Summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n{text}",
    input_variables=['text']
)

# StringOutputParser

parser = StrOutputParser()

# Form a Chain (Pipeline)
chain = template1 | model | parser | template2 | model | parser
# invoke chain and store it in a variable
result = chain.invoke({'topic':'black hole'})
# print the reasult
print(result)


