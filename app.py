# import streamlit as st
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

import streamlit as st
from PIL import Image
from components.fundamentals import show_fundamentals, show_gdp_chart, show_pmi_chart, show_interest_rate_chart
from components.sentiment import show_sentiment, show_cot_report
from components.news_summarizer import news_summarizer_tab

# Set the page config for layout and title
st.set_page_config(page_title="Escavic", layout="wide")

# Custom CSS for black and white theme with premium styling
st.markdown("""
    <style>
    /* Set the background color of the entire app to black */
    .reportview-container {
        background: #000000;  /* Black background */
    }
    .sidebar .sidebar-content {
        background: #111111;  /* Dark grey sidebar */
    }
    
    /* Set the font color to white for text */
    body {
        color: white;
    }
    
    /* Style headings */
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
    }
    
    h1 {
        font-size: 36px;
    }

    h2 {
        font-size: 24px;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #ffffff;  /* White background for buttons */
        color: #000000;  /* Black text */
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px 24px;
        border: 2px solid #ffffff;  /* White border for buttons */
        transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #000000;  /* Black background on hover */
        color: #ffffff;  /* White text on hover */
    }

    /* Expander Styling */
    .stExpander>details {
        background-color: #333333;
        color: #ffffff;
        font-weight: bold;
    }
    .stExpander>details[open] {
        background-color: #444444;
    }
    
    /* Slider Styling */
    .stSlider>div>div {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Image Styling */
    .stImage>img {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    
    /* Sidebar Title */
    .sidebar .sidebar-content h1 {
        color: #ffffff;
    }
    
    /* Tables Styling */
    .stTable th {
        background-color: #333333;
        color: white;
    }
    .stTable td {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Layout for Logo and Title
col1, col2 = st.columns([1, 8])
with col1:
    logo = Image.open("assets/escavic.png")
    st.image(logo, width=160)  # slightly smaller = cleaner

with col2:
    st.markdown(
        """
        <div style='padding-top: 10px;'>
            <h1 style='margin-bottom: 0; font-size: 36px;'>Escavic</h1>
            <p style='color: grey; font-size: 18px; margin-top: 0;'>Macro, Sentiment & News in One Dashboard</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 3️⃣ Now start your Sidebar
st.sidebar.title("Escavic")

st.sidebar.markdown("""
**About:**  
Escavic is a powerful dashboard for Forex traders, providing real-time **fundamental** and **sentiment** analysis in one place.    
Build by the **Traders** for the **Traders**.    
Let's Escape to the **VICTORY**!
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
    with st.expander("View COT Report"):
        show_cot_report()

elif tab == "🧠 News Summarizer":
    news_summarizer_tab()
