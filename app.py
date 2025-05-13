import streamlit as st
# from PIL import Image
# from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
# from components.sentiment import show_sentiment, show_cot_report # 👈 import upar laa diya
# from components.news_summarizer import news_summarizer_tab


# st.set_page_config(page_title="Escavic", layout="wide")
# col1, col2 = st.columns([1, 8])

# with col1:
#     logo = Image.open("assets/escavic.png")
#     st.image(logo, width=160)  # slightly smaller = cleaner

# with col2:
#     st.markdown(
#         """
#         <div style='padding-top: 10px;'>
#             <h1 style='margin-bottom: 0; font-size: 36px;'>Escavic</h1>
#             <p style='color: grey; font-size: 18px; margin-top: 0;'>Macro, Sentiment & News in One Dashboard</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # 3️⃣ Now start your Sidebar
# st.sidebar.title("Escavic")

# st.sidebar.markdown("""
# **About:**  
# Escavic is a powerful dashboard for Forex traders, providing real-time **fundamental** and **sentiment** analysis in one place.    
# Build by the **Traders** for the **Traders**.    
# Let's Escape to the **VICTORY**!
# """)
# tab = st.sidebar.radio("Select Section", ["🌍 Fundamentals", "📈 Sentiment", "🧠 News Summarizer"])

# if tab == "🌍 Fundamentals":
#     st.header("Fundamental Analysis")
#     show_fundamentals()
    
#     with st.expander("View GDP Growth Rate"):
#         show_gdp_chart()

#     with st.expander("View PMI Index"):
#         show_pmi_chart()

#     with st.expander("View Interest Rate"):
#         show_interest_rate_chart()

# elif tab == "📈 Sentiment":
#     st.header("Sentiment Analysis")
#     show_sentiment()
#     with st.expander("View COT Report"):
#         show_cot_report()
# elif tab == "🧠 News Summarizer":
#     news_summarizer_tab()
from components import fundamentals, news_summarizer, sentiment

st.set_page_config(page_title="Escavic Dashboard", layout="wide")
st.title("📊 Escavic – Forex Intelligence Dashboard")

page = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Fundamental Data", "Sentiment Data", "News Summarizer"]
)

if page == "Home":
    st.markdown("### Welcome to Escavic")
    st.markdown("Use the sidebar to navigate through the dashboard features.")
    st.markdown("Built by Rovin and Team 🚀")
elif page == "Fundamental Data":
    fundamentals.show_fundamentals()
elif page == "Sentiment Data":
    sentiment.show_sentiment()
elif page == "News Summarizer":
    news_summarizer.show_news_summarizer_tab()
