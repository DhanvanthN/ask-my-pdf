import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain
from transformers import pipeline

# App config
st.set_page_config(page_title="📄 AskYourPDF", layout="centered")
st.markdown("""
    <h1 style='text-align: center;'>📄 AskYourPDF</h1>
    <p style='text-align: center;'>Upload a PDF, ask questions, get instant answers from a local LLM 🔥</p>
""", unsafe_allow_html=True)

# Upload PDF
pdf = st.file_uploader("📎 Upload your PDF file", type="pdf")

if pdf is not None:
    st.success(f"✅ Uploaded: `{pdf.name}`")

    with st.spinner("🔍 Reading and processing your PDF..."):
        # Read PDF content
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split text into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Generate embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Ask user question
    user_question = st.text_input("🤔 Ask a question about the PDF")

    if user_question:
        with st.spinner("🧠 Thinking..."):
            docs = knowledge_base.similarity_search(user_question)

            # Load FLAN-T5 base model
            qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
            llm = HuggingFacePipeline(pipeline=qa_pipeline)

            # Run QA chain
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)

        # Show result
        st.markdown("### ✅ Answer")
        st.success(response)

else:
    st.info("👆 Please upload a PDF file to start querying.")

