import streamlit as st
from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
from components.sentiment import show_sentiment  # 👈 import upar laa diya

st.set_page_config(page_title="TradeScope AI", layout="wide")

st.sidebar.title("📊 TradeScope AI")
tab = st.sidebar.radio("Select Section", ["🌍 Fundamentals", "📈 Sentiment", "🧠 News Summarizer"])

if tab == "🌍 Fundamentals":
    st.header("Fundamental Analysis")
    show_fundamentals()
    
    with st.expander("View GDP Growth Rate"):
        show_gdp_chart()

    with st.expander("View PMI Index"):
        show_pmi_chart()

    with st.expander("View Interest Rate"):
        show_interest_rate_chart()

elif tab == "📈 Sentiment":
    st.header("Sentiment Analysis")
    show_sentiment()

elif tab == "🧠 News Summarizer":
    st.header("News Summarizer")
    st.write("This section will show AI-based news summaries.")
