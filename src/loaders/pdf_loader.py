from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdfs(pdf_paths):
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        pages = loader.load()
        chunks = splitter.split_documents(pages)
        docs.extend(chunks)
    return docs
