from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import  RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()
# Model
model = ChatOpenAI()
# Output Parser
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')
# Pydantic OutputParser
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt1
prompt1 = PromptTemplate(
    template="Classify the sentiment of the follwing feedback into positive or negative \n {feedback}",
    input_variables=['feedback']
)
# Chain
classifier_chain = prompt1 | model | parser2
# result =  classifier_chain.invoke({'feedback':'this is a terrible smartphone'}).sentiment # It is not confirm that model will give positive or negative feedback
# print(result)

# we have to use Branching using RunnablBranch
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n{feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n{feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x['sentiment']=='positive', prompt2 | model | parser),
    (lambda x:x['sentiment']=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment") # Branch Chain using Runnable0Lambda
)

chain = classifier_chain | branch_chain
print(chain.invoke({'feedback':'This is a terrible phone'}))
print(chain.get_graph().print_ascii())