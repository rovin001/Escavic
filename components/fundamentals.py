import pandas as pd
import streamlit as st

def show_fundamentals():
    st.subheader("📉 Inflation Rate (CPI)")
    df = pd.read_csv("data/cpi_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    st.line_chart(df.set_index('Date')['InflationRate'])
