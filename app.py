import streamlit as st
from transformers import pipeline
from pdfminer.high_level import extract_text

def extract_resume_text(file):
    return extract_text(file)

def generate_questions(resume_text):
    summarizer = pipeline("summarization")
    summary = summarizer(resume_text)[0]['summary_text']
    return f"Generated interview questions based on your resume: {summary}"

st.title("Resume-based Question Generator")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])
if uploaded_file is not None:
    resume_text = extract_resume_text(uploaded_file)
    st.write("Resume Text:", resume_text)
    questions = generate_questions(resume_text)
    st.write(questions)