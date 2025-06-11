from langchain_community.document_loaders import PyPDFLoader
import os

# PyPDf Loader But not that efficient 
# wher we have textual data in our pdf 
# if we have scaneed images then we have to user other pdf loaders

# Simple pdf loader = PypdfLoader
# PDFs with tables/columns- PDFlumberloader
# PDFs with scanned/images- UnstructuredPDFloader / AmazonTextractPDFloader
# Need Layout and images- PyMuPDfloader
# With text structured extraction- UnstructuredPDFloader

pdf_file_path = r"E:\15_CampusX_LangChain\10.Documents_Loaders\DocumentClassification using LayoutLMv3.pdf"
loader = PyPDFLoader(pdf_file_path)
docs = loader.load()

print("Pages in pdf: ",len(docs))
print('*'*50)
print(docs[2].page_content)
print(docs[1].metadata)
