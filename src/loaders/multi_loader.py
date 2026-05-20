from langchain_community.document_loaders import PyPDFLoader, CSVLoader, WebBaseLoader

# PDF
pdf_loader = PyPDFLoader("data/company_policy.pdf")   # <-- synthetic PDF we generated
pdf_docs = pdf_loader.load()

# CSV
csv_loader = CSVLoader("data/product_faq.csv", source_column="question")
csv_docs = csv_loader.load()

# Web
web_loader = WebBaseLoader("https://docs.python.org/3/")
web_docs = web_loader.load()

# Merge
all_docs = pdf_docs + csv_docs + web_docs
print(f"PDF docs: {len(pdf_docs)}")
print(f"CSV docs: {len(csv_docs)}")
print(f"Web docs: {len(web_docs)}")
print(f"Total merged docs: {len(all_docs)}")
