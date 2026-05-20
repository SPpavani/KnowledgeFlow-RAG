from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = FAISS.load_local("faiss_index", embeddings)

retriever = db.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "Summarize the AI strategy 2024 document."
answer = qa.run(query)
print("Q:", query)
print("A:", answer)
