import pandas as pd
import streamlit as st

def show_sentiment():
    st.subheader("📈 Broker Sentiment Data")
    df = pd.read_csv("data/sentiment_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    st.dataframe(df)

    st.subheader("📊 Buy vs Sell Orders Over Time")
    st.line_chart(df.set_index('Date')[['Buy Orders', 'Sell Orders']])
