from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader = DirectoryLoader(
    path=r"E:\15_CampusX_LangChain\10.Documents_Loaders\Book",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# 'loader'
# docs = loader.load()
# print("Number of Documents: ",len(docs))
# print(docs[0].page_content)
# print(docs[1].metadata)

# It is taking time to load the data so imagine that we have 100 of pdf 
# the at that time we can use 'lazy load' functionality using langchain


# | Aspect           | `load()`                        | `lazy_load()`                               |
# | ---------------- | ------------------------------- | ------------------------------------------- |
# | **Type**         | Eager loading (all at once)     | Lazy loading (streaming/generator)          |
# | **Returns**      | `List[Document]`                | `Iterator[Document]`                        |
# | **Memory usage** | High (loads all into memory)    | Low (loads one at a time)                   |
# | **Performance**  | Faster for small files          | Scales better for large files or many files |
# | **Use case**     | Small files, fast access needed | Large files, batch processing, low RAM      |


# Lazy Loader implemention
docs = loader.lazy_load()
for document in docs:
    print(document.metadata)
