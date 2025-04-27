import streamlit as st
from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
from components.sentiment import show_sentiment  # 👈 import upar laa diya
from components.news_summarizer import news_summarizer_tab
from PIL import Image  # for local image loading

# 1️⃣ Load your logo
logo = Image.open("assets/logo.png")

# 2️⃣ Display it centered with title & subtitle
st.markdown(
    """
    <div style="display:flex; flex-direction:column; align-items:center; padding:10px 0;">
      <img src="assets/logo.png" width="120" />
      <h1 style="margin:5px 0;">TradeScope AI</h1>
      <p style="margin:0; color:#555;">Macro, Sentiment & News in One Dashboard</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="TradeScope AI", layout="wide")

st.sidebar.title("📊 TradeScope AI")
st.sidebar.markdown("""
**About:**  
TradeScope AI is a powerful dashboard for Forex traders, providing real-time **fundamental** and **sentiment** analysis in one place.  
Built by the **Traders** for the **Traders**!
Let's Escape to the **VICTORY**
""")
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
    news_summarizer_tab()
