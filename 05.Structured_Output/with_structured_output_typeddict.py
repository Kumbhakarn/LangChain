# Text Splitting
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated, Optional, Literal


load_dotenv()
model = ChatOpenAI()

# Schema
class Review(TypedDict):
    # simple TypedDict
    summary: str
    sentiment: str

structured_model= model.with_structured_output(Review)

result = structured_model.invoke("""
The KeyChron K8 Wireless Mechanical Keyboard is a solid mid-range option for anyone looking to upgrade 
their typing or gaming setup with a reliable and customizable mechanical keyboard. After using it for over a month, here’s my take
""")

print(result)
print(result['summary'])
print(result['sentiment'])


# ---Annotation---

# class Review(TypedDict):
#     
#     summary: Annotated([str,'A Brief summary of the review'])
#     sentiment: Annotated[str,'Return sentiment of the review either negative,positev or neutral']

# structured_model= model.with_structured_output(Review)
# result = structured_model.invoke("""
# The KeyChron K8 Wireless Mechanical Keyboard is a solid mid-range option for anyone looking to upgrade 
# their typing or gaming setup with a reliable and customizable mechanical keyboard. After using it for over a month, here’s my take
# """)

# print(result)
# print(result['summary'])
# print(result['sentiment'])


# ---More Detailed---

# model = ChatOpenAI()

# # Schema
# class Review(TypedDict):
#     Key_things: Annotated[list[str],"Write down all the key themesdiscussed in the review in a list"]
#     summary: Annotated[str,'A brief summary of the review']
#     sentiment: Annotated[Literal['pos','neg],'Return sentiment of the review either negative, positive or netural'] # To check sentiment pos or negative
#     pros: Annotated[Optional[list[str]],'Write down all the pros inside a list']
#     cons: Annotated[Optional[list[str]],'Write down all the cons inside a list']
#     name: Annotated[Optional[str],'Write the name of the reviewer']
    
# structured_model= model.with_structured_output(Review)

# result = structured_model.invoke("""
# The KeyChron K8 Wireless Mechanical Keyboard is a solid mid-range option for anyone looking to upgrade 
# their typing or gaming setup with a reliable and customizable mechanical keyboard. After using it for over a month, here’s my take
# """)
  
# print(result)
# print(result['summary'])
# print(result['sentiment'])
# print(result.keys)
