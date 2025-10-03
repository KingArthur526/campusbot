from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = DirectoryLoader("docs", glob = "*.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 300, chunk_overlap = 50)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(chunks, embeddings)

def need_context(query: str, k: int=2):
    docs = vectorstore.similarity_search(query,k=k)
    return " ".join(doc.page_content for doc in docs)