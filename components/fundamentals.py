import pandas as pd
import altair as alt
import streamlit as st

def show_fundamentals():
    st.subheader("📉 Inflation Rate (CPI)")

    # Reading CPI data from CSV
    df = pd.read_csv("data/cpi_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    # Altair chart with horizontal scrolling and no zoom
    cpi_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('InflationRate:Q', title='Inflation Rate (%)'),
        tooltip=['Date', 'InflationRate']
    ).properties(
        width=800,  # Fixed width for the chart
        height=400,
        title="CPI Inflation Rate Over Time"
    ).interactive(bind_y=False)  # Disable Y-axis zooming

    st.altair_chart(cpi_chart, use_container_width=True)

def show_gdp_chart():
    st.subheader("GDP Growth Rate Over Time")
    df = pd.read_csv('data/gdp_data.csv')
    
    gdp_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('GDPGrowth:Q', title='GDP Growth Rate (%)'),
        tooltip=['Date', 'GDPGrowth']
    ).properties(
        width=800,
        height=400,
        title="GDP Growth Rate Over Time"
    ).interactive(bind_y=False)

    st.altair_chart(gdp_chart, use_container_width=True)

def show_pmi_chart():
    st.subheader("PMI Index Over Time")
    df = pd.read_csv('data/pmi_data.csv')
    
    pmi_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('PMI:Q', title='PMI Index'),
        tooltip=['Date', 'PMI']
    ).properties(
        width=800,
        height=400,
        title="PMI Index Over Time"
    ).interactive(bind_y=False)

    st.altair_chart(pmi_chart, use_container_width=True)

def show_interest_rate_chart():
    st.subheader("Interest Rate Over Time")
    df = pd.read_csv('data/interest_rate_data.csv')
    
    interest_rate_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('InterestRate:Q', title='Interest Rate (%)'),
        tooltip=['Date', 'InterestRate']
    ).properties(
        width=800,
        height=400,
        title="Interest Rate Over Time"
    ).interactive(bind_y=False)

    st.altair_chart(interest_rate_chart, use_container_width=True)
