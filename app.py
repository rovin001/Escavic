import streamlit as st

st.set_page_config(page_title="TradeScope AI", layout="wide")

st.sidebar.title("📊 TradeScope AI")
tab = st.sidebar.radio("Select Section", ["🌍 Fundamentals", "📈 Sentiment", "🧠 News Summarizer"])

if tab == "🌍 Fundamentals":
    st.header("Fundamental Analysis")
    st.write("CPI, Interest Rate, GDP Data etc. will be shown here.")
elif tab == "📈 Sentiment":
    st.header("Sentiment Analysis")
    st.write("Broker reports and order flow sentiment here.")
elif tab == "🧠 News Summarizer":
    st.header("News Summarizer")
    st.write("This section will show AI-based news summaries.")
from components.fundamentals import show_fundamentals

if tab == "🌍 Fundamentals":
    st.header("Fundamental Analysis")
    show_fundamentals()
