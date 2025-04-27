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

    # Melt data to combine Buy and Sell Orders for bar chart
    melted_df = broker_df.melt(id_vars=['Date'], value_vars=['Buy Orders', 'Sell Orders'],
                               var_name='Order Type', value_name='Order Count')

    # Plot both Buy and Sell in same graph
    bar_chart = alt.Chart(melted_df).mark_bar().encode(
        x=alt.X('Date:O', title='Date'),
        y=alt.Y('Order Count:Q', title='Number of Orders'),
        color=alt.Color('Order Type:N', scale=alt.Scale(domain=['Buy Orders', 'Sell Orders'],
                                                        range=['#1f77b4', '#ff7f0e'])),
        tooltip=['Date', 'Order Type', 'Order Count']
    ).properties(
        width=700,
        height=400,
        title='Buy vs Sell Orders'
    )

    st.altair_chart(bar_chart, use_container_width=True)
def show_cot_report():
    st.subheader("🗂️ COT Report (Longs vs Shorts)")
    df = pd.read_csv("data/cot_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    # Melt so we can plot both series in one chart
    cot = df.melt(id_vars=['Date'], value_vars=['Longs','Shorts'],
                  var_name='Position', value_name='Contracts')
    chart = (
        alt.Chart(cot)
           .mark_line(point=True)
           .encode(
               x=alt.X('Date:T', title='Date', axis=alt.Axis(labelAngle=-45)),
               y=alt.Y('Contracts:Q', title='Number of Contracts'),
               color='Position:N',
               tooltip=['Date','Position','Contracts']
           )
           .properties(width=800, height=350, title="COT Longs vs Shorts Over Time")
    )
    st.altair_chart(chart, use_container_width=True)
