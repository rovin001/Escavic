import streamlit as st
from PIL import Image
from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
from components.sentiment import show_sentiment  # 👈 import upar laa diya
from components.news_summarizer import news_summarizer_tab


st.set_page_config(page_title="TradeScope AI", layout="wide")
col1, col2 = st.columns([1, 8])

with col1:
    logo = Image.open("assets/escavic_logo.png")
    st.image(logo, width=160)  # slightly smaller = cleaner

with col2:
    st.markdown(
        """
        <div style='padding-top: 10px;'>
            <h1 style='margin-bottom: 0; font-size: 36px;'>TradeScope AI</h1>
            <p style='color: grey; font-size: 18px; margin-top: 0;'>Macro, Sentiment & News in One Dashboard</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 3️⃣ Now start your Sidebar
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
