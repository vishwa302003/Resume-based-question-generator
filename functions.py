from pdfminer.high_level import extract_text
from transformers import pipeline

def extract_resume_text(file):
    return extract_text(file)

def generate_questions(resume_text):
    summarizer = pipeline("summarization")
    summary = summarizer(resume_text)[0]['summary_text']
    return f"Generated interview questions based on your resume: {summary}"