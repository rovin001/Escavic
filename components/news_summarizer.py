import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarize_with_t5(text: str) -> str:
    # Split text into chunks to ensure the length is manageable for the model
    chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
    summary = ""
    
    for chunk in chunks:
        out = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
        summary += out + " "
        
    return summary.strip()
