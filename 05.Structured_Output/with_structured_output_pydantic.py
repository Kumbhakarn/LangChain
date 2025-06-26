# Structured Output Pydandic 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict,Annotated, Optional, Literal


load_dotenv()
model = ChatOpenAI()

# Schema
class Review(BaseModel):

    key_themes: list[str] = Field(description='Write down all the key themesdiscussed in the review in a list')
    summary: str = Field(description='A brief summary of the review')
    sentiment: Literal['pos','neg'] = Field(description='Return Sentiment of the review sentiment of the review either negative, positive or netural')
    pros: Optional[list[str]] = Field(default=None,description='Write down all the pros inside a list')
    cons: Optional[list[str]] = Field(default=None,description='Write down all the cons inside a list')
    name: Optional[str] = Field(default=None,description='Write the name of the reviewer')

structured_model= model.with_structured_output(Review)

result = structured_model.invoke("""
The KeyChron K8 Wireless Mechanical Keyboard is a solid mid-range option for anyone looking to upgrade 
their typing or gaming setup with a reliable and customizable mechanical keyboard. After using it for over a month, here’s my take
""")

print(result.name)
print(result)
