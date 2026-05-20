from src.loaders.multi_loader import all_docs   # <-- use merged docs
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS, Pinecone, Weaviate
import pinecone, weaviate

# Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# --- Option 1: FAISS (local) ---
faiss_db = FAISS.from_documents(all_docs, embeddings)
faiss_db.save_local("faiss_index")

# --- Option 2: Pinecone (cloud) ---
pinecone.init(api_key="YOUR_PINECONE_KEY", environment="us-west1-gcp")
pinecone_db = Pinecone.from_documents(all_docs, embeddings, index_name="policy-index")

# --- Option 3: Weaviate (semantic graph) ---
client = weaviate.Client("https://your-weaviate-instance")
weaviate_db = Weaviate.from_documents(all_docs, embeddings, client=client, index_name="PolicyDocs")

print("Vector stores created successfully with PDF + CSV + Web sources!")
