from langchain_community.document_loaders import WebBaseLoader,SeleniumURLLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

# import a model
model = ChatGroq(
    model_name = "llama3-8b-8192",
    temperature=0.5,
    streaming=False
)

# Write a prompt 
prompt = PromptTemplate(
    template="Answer the fallowing \n {question} from the fallowing text - \n {text}",
    input_variables=['question','text']
)

# OutputParser stroutput parser
parser = StrOutputParser()


# Webbase loader import website url from here
url='https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw0w3hn-a/p/itmf733f99c22ee6?pid=COMH9ZWQP4EP2XAT&lid=LSTCOMH9ZWQP4EP2XAT2OHHOE&marketplace=FLIPKART&q=macbook+air+m4&store=6bo%2Fb5g&spotlightTagId=default_TrendingId_6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=search-autosuggest&iid=e0b3a98e-5ae8-491f-bc9e-04157e46a066.COMH9ZWQP4EP2XAT.SEARCH&ppt=sp&ppn=sp&ssid=i8ld4wisfk0000001749449423200&qH=a3dc101ea3bce06d'
loader = WebBaseLoader(url)
# we can pass list of url as well 
docs = loader.load()


# print(len(docs))
# print(docs[0].page_content)

# form a chain
chain = prompt | model | parser

# invoke the chain
print(chain.invoke({'question': 'What is the product name?','text':docs[0].page_content}))