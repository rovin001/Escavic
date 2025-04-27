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
def news_summarizer_tab():
    st.header("🧠 News Summarizer")
    
    choice = st.radio("Choose Input Type", ["Paste Article", "Fetch Live News"])
    
    if choice == "Paste Article":
        text = st.text_area("Paste your article here", height=200)
    elif choice == "Fetch Live News":
        # Placeholder for fetching live news (can later add functionality to pull news from APIs)
        text = "Live Forex Article goes here."  # Placeholder text
        st.write("Live Forex News (simulated):")
        st.write(text[:200] + "...")
    
    if st.button("Summarize"):
        if text.strip() != "":
            with st.spinner("Generating summary..."):
                summary = summarize_with_t5(text)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.error("Please enter or fetch an article.")
