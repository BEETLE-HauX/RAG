# core.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

class LectureProcessor:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="llama3")
        self.llm = Ollama(model="llama3")
        
    def load_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        return loader.load()
    
    def chunk_text(self, docs):
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return splitter.split_documents(docs)
    
    def create_vectorstore(self, chunks):
        return FAISS.from_documents(chunks, self.embeddings)
    
    def generate_summary(self, text):
        prompt = ChatPromptTemplate.from_template("""
        Summarize this lecture material in 3-5 bullet points:
        {text}
        """)
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(text=text)
    
    def generate_qa_pairs(self, text):
        prompt = ChatPromptTemplate.from_template("""
        Generate 3 FAQs and answers from this text:
        {text}
        Format as: Q: [question]\nA: [answer]\n\n
        """)
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(text=text)