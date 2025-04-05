import streamlit as st
from utils.rag import RAGSystem

rag = RAGSystem()

def knowledge_base_ui():
    st.title("Project Knowledge Base")
    
    # Document Upload
    uploaded_file = st.file_uploader("Add documentation")
    if uploaded_file:
        with open(f"data/knowledge_base/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        rag.add_document(f.name)
        st.success("Document indexed!")
    
    # Query Interface
    query = st.text_input("Ask about the project")
    if query:
        results = rag.query(query)
        st.write(results)