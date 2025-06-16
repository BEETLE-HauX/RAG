# app.py
import streamlit as st
from core import LectureProcessor
import tempfile

processor = LectureProcessor()

st.title("📚 Lecture Summarizer & Quiz Generator")
uploaded_file = st.file_uploader("Upload lecture slides (PDF)", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        docs = processor.load_pdf(tmp.name)
    
    chunks = processor.chunk_text(docs)
    vectorstore = processor.create_vectorstore(chunks)
    
    with st.spinner("Processing..."):
        # Get first page for demo
        first_page = docs[0].page_content
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Summary")
            st.write(processor.generate_summary(first_page))
            
        with col2:
            st.subheader("FAQs")
            st.write(processor.generate_qa_pairs(first_page))