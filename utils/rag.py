from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

class RAGSystem:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="llama3")
        self.db = Chroma(persist_directory="data/knowledge_base", embedding_function=self.embeddings)
    
    def add_document(self, file_path):
        with open(file_path) as f:
            text = f.read()
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
        docs = splitter.create_documents([text])
        self.db.add_documents(docs)
    
    def query(self, question):
        results = self.db.similarity_search(question, k=3)
        return "\n\n".join([r.page_content for r in results])