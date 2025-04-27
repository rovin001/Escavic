import pandas as pd
import streamlit as st
import altair as alt

def show_sentiment():
    st.subheader("Broker Sentiment Overview 📈")
    df = pd.read_csv('data/sentiment_data.csv')

    # Select broker
    brokers = df['Broker Name'].unique()
    selected_broker = st.selectbox("Select a Broker", brokers)

    # Filter data for the selected broker
    broker_df = df[df['Broker Name'] == selected_broker]

    st.write(f"Showing Sentiment Data for: **{selected_broker}**")

    # Make a bar chart
    melted_df = broker_df.melt(id_vars=['Date'], value_vars=['Buy Orders', 'Sell Orders'],
                               var_name='Order Type', value_name='Order Count')

    bar_chart = alt.Chart(melted_df).mark_bar().encode(
        x='Date:O',
        y='Order Count:Q',
        color='Order Type:N',
        column='Order Type:N'
    ).properties(
        width=150,
        height=300
    )

    st.altair_chart(bar_chart, use_container_width=True)
