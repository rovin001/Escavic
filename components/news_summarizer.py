# # components/news_summarizer.py

# import streamlit as st
# from transformers import pipeline

# @st.cache_resource
# def load_summarizer():
#     return pipeline("summarization", model="t5-small")

# def news_summarizer_tab():
#     st.header("🧠 News Summarizer")
#     summarizer = load_summarizer()

#     choice = st.radio("Choose Input Type", ["Paste Article", "Fetch Live"])
#     if choice == "Paste Article":
#         text = st.text_area("Paste your article here", height=200)
#     else:
#         # placeholder or your fetch function
#         text = "Simulated live forex news article..."
#         st.write(text)

#     if st.button("Summarize"):
#         if not text.strip():
#             st.error("Please enter or fetch an article.")
#             return
#         with st.spinner("Generating summary..."):
#             # split into chunks if very long
#             chunks = [text[i:i+500] for i in range(0, len(text), 500)]
#             summary = " ".join(
#                 summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
#                 for chunk in chunks
#             )
#         st.subheader("Summary")
#         st.write(summary)
import streamlit as st
from transformers import pipeline

# Initialize the summarizer
summarizer = pipeline("summarization", model="t5-small")

# Function for News Summarizer
def news_summarizer_tab():
    st.header("News Summarizer")
    
    # Option for the user to choose input type
    choice = st.radio("Choose Input Method", ["Paste Article", "Fetch Live News"])

    # Layout with two columns
    col1, col2 = st.columns(2)
    
    # Column 1: Paste Article
    with col1:
        if choice == "Paste Article":
            text = st.text_area("Paste your article here", height=200)

    # Column 2: Fetch Live News
    with col2:
        if choice == "Fetch Live News":
            # For the live news, use a placeholder or API fetch
            live_text = "This is where your live news content will appear..."  # Replace with live news fetch logic
            st.write("**Live News Preview:**")
            st.write(live_text[:200] + "…")

    # Summarizer Button and Logic
    with st.expander("Generate Summary"):
        if st.button("Summarize"):
            if choice == "Paste Article" and text:
                summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
                st.subheader("Summary")
                st.write(summary[0]['summary_text'])
            elif choice == "Fetch Live News" and live_text:
                summary = summarizer(live_text, max_length=150, min_length=50, do_sample=False)
                st.subheader("Summary")
                st.write(summary[0]['summary_text'])

# Calling the function
news_summarizer_tab()
