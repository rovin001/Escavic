import pandas as pd
import streamlit as st

def show_fundamentals():
    st.subheader("📉 Inflation Rate (CPI)")
    df = pd.read_csv("data/cpi_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    st.line_chart(df.set_index('Date')['InflationRate'])
import pandas as pd
import streamlit as st

def show_gdp_chart():
    st.subheader("GDP Growth Rate Over Time")
    df = pd.read_csv('data/gdp_data.csv')
    st.line_chart(df.set_index('Date'))

def show_pmi_chart():
    st.subheader("PMI Index Over Time")
    df = pd.read_csv('data/pmi_data.csv')
    st.line_chart(df.set_index('Date'))

def show_interest_rate_chart():
    st.subheader("Interest Rate Over Time")
    df = pd.read_csv('data/interest_rate_data.csv')
    st.line_chart(df.set_index('Date'))
