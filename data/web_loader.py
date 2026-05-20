from langchain_community.document_loaders import WebBaseLoader

# ── LOAD WEB DOCS ────────────────────────────────────────────────
web_loader = WebBaseLoader("https://docs.python.org/3/")
web_docs = web_loader.load()

print(f"Web docs loaded: {len(web_docs)}")
