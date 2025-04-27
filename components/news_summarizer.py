# components/news_summarizer.py

import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small")

def news_summarizer_tab():
    st.header("News Summarizer")
    summarizer = load_summarizer()

    choice = st.radio("Choose Input Type", ["Paste Article", "Fetch Live"])
    if choice == "Paste Article":
        text = st.text_area("Paste your article here", height=200)
    else:
        # placeholder or your fetch function
        text = "Simulated live forex news article..."
        st.write(text)

    if st.button("Summarize"):
        if not text.strip():
            st.error("Please enter or fetch an article.")
            return
        with st.spinner("Generating summary..."):
            # split into chunks if very long
            chunks = [text[i:i+500] for i in range(0, len(text), 500)]
            summary = " ".join(
                summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
                for chunk in chunks
            )
        st.subheader("Summary")
        st.write(summary)

