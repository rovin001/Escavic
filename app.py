import streamlit as st
from PIL import Image
from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
from components.sentiment import show_sentiment  # 👈 import upar laa diya
from components.news_summarizer import news_summarizer_tab


st.set_page_config(page_title="TradeScope AI", layout="wide")
st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .header-logo img {
        width: 70px; /* Logo size */
        height: auto;
    }
    .header-text h1 {
        margin-bottom: 0px;
    }
    .header-text p {
        margin-top: 0px;
        color: grey;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout
st.markdown(
    """
    <div class="header-container">
        <div class="header-logo">
            <img src="assets/escavic.png" alt="Logo">
        </div>
        <div class="header-text">
            <h1>TradeScope AI</h1>
            <p>Macro, Sentiment & News in One Dashboard</p>
        </div>
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
