from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"E:\15_CampusX_LangChain\10.Documents_Loaders\Bengaluru_House_Data.csv")
docs = loader.load()
print("Single Document Objec: 1st row: ",docs[0])
print('*'*50)
print("Single Document Objec: 2nd row: ",docs[1])
print('*'*50)
print("Number of rows: ",len(docs))

# it makes every row one doc object