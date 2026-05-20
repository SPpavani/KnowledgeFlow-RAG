# ── IMPORTS ────────────────────────────────────────────────
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, WebBaseLoader

# ── LOAD PDF ────────────────────────────────────────────────
pdf_loader = PyPDFLoader("data/company_policy.pdf")   # <-- make sure this file exists
pdf_docs = pdf_loader.load()
print(f"PDF docs: {len(pdf_docs)}")

# ── LOAD CSV ────────────────────────────────────────────────
csv_loader = CSVLoader("data/product_faq.csv", source_column="question")  # <-- make sure this file exists
csv_docs = csv_loader.load()
print(f"CSV docs: {len(csv_docs)}")

# ── LOAD WEB DOCS ────────────────────────────────────────────────
web_loader = WebBaseLoader("https://docs.yourcompany.com/api")  # <-- replace with a real URL
web_docs = web_loader.load()
print(f"Web docs: {len(web_docs)}")

# ── MERGE SOURCES ────────────────────────────────────────────────
all_docs = pdf_docs + csv_docs + web_docs
print(f"Total merged docs: {len(all_docs)}")
