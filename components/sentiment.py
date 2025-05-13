# import pandas as pd
# import streamlit as st
# import altair as alt

# def show_sentiment():
#     st.subheader("Broker Sentiment Overview 📈")
#     df = pd.read_csv('data/sentiment_data.csv')

#     # Select broker
#     brokers = df['Broker Name'].unique()
#     selected_broker = st.selectbox("Select a Broker", brokers)

#     # Filter data for the selected broker
#     broker_df = df[df['Broker Name'] == selected_broker]

#     st.write(f"Showing Sentiment Data for: **{selected_broker}**")

#     # Melt data to combine Buy and Sell Orders for bar chart
#     melted_df = broker_df.melt(id_vars=['Date'], value_vars=['Buy Orders', 'Sell Orders'],
#                                var_name='Order Type', value_name='Order Count')

#     # Plot both Buy and Sell in same graph
#     bar_chart = alt.Chart(melted_df).mark_bar().encode(
#         x=alt.X('Date:O', title='Date'),
#         y=alt.Y('Order Count:Q', title='Number of Orders'),
#         color=alt.Color('Order Type:N', scale=alt.Scale(domain=['Buy Orders', 'Sell Orders'],
#                                                         range=['#1f77b4', '#ff7f0e'])),
#         tooltip=['Date', 'Order Type', 'Order Count']
#     ).properties(
#         width=700,
#         height=400,
#         title='Buy vs Sell Orders'
#     )

#     st.altair_chart(bar_chart, use_container_width=True)
# def show_cot_report():
#     st.subheader("🗂️ COT Report — Longs vs Shorts")

#     # Load the data
#     df = pd.read_csv('data/cot_data.csv')
#     df['Date'] = pd.to_datetime(df['Date'])
#     df['Month'] = df['Date'].dt.strftime('%Y-%m')

#     # Select Currency Pair
#     pairs = df['Currency Pair'].unique()
#     selected_pair = st.selectbox("Select Currency Pair", pairs)

#     # Filter by selected pair
#     pair_df = df[df['Currency Pair'] == selected_pair]

#     # Melt the data for plotting
#     melted_cot = pair_df.melt(
#         id_vars=['Month'],
#         value_vars=['Long Positions', 'Short Positions'],
#         var_name='Position',
#         value_name='Contracts'
#     )

#     # Plot the chart
#     cot_chart = (
#         alt.Chart(melted_cot)
#             .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
#             .encode(
#                 x=alt.X('Month:N', title='Month', axis=alt.Axis(labelAngle=-45)),
#                 y=alt.Y('Contracts:Q', title='Number of Contracts', stack='zero'),
#                 color=alt.Color(
#                     'Position:N',
#                     scale=alt.Scale(domain=['Long Positions', 'Short Positions'], range=['#1f77b4', '#ff7f0e']),
#                     legend=alt.Legend(title="Position")
#                 ),
#                 tooltip=['Month', 'Position', 'Contracts']
#             )
#             .properties(
#                 width=700,
#                 height=400,
#                 title=f'COT Long vs Short Positions for {selected_pair}'
#             )
#     )

#     st.altair_chart(cot_chart, use_container_width=True)

import pandas as pd
import streamlit as st
import altair as alt

def show_sentiment():
    st.subheader("Broker Sentiment Overview 📈")
    df = pd.read_csv('data/sentimental_data/sentiment_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort data to show latest first
    df = df.sort_values('Date', ascending=False)

    # Currency pair sentiment summary
    st.markdown("### Sentiment Signal by Currency Pair 🧭")
    sentiment_summary = df.groupby('Currency Pair').agg({
        'Buy Orders': 'sum',
        'Sell Orders': 'sum'
    }).reset_index()

    sentiment_summary['Bias'] = sentiment_summary.apply(
        lambda row: '📈 Buy' if row['Buy Orders'] > row['Sell Orders'] else '📉 Sell', axis=1
    )

    st.dataframe(sentiment_summary[['Currency Pair', 'Buy Orders', 'Sell Orders', 'Bias']], use_container_width=True)

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
        x=alt.X('Date:O', title='Date', sort='descending'),
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
    st.subheader("🗂️ COT Report — Longs vs Shorts")

    # Load the data
    df = pd.read_csv('data/sentimental_data/cot_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')

    # Select Currency Pair
    pairs = df['Currency Pair'].unique()
    selected_pair = st.selectbox("Select Currency Pair", pairs)

    # Filter by selected pair
    pair_df = df[df['Currency Pair'] == selected_pair]

    # Melt the data for plotting
    melted_cot = pair_df.melt(
        id_vars=['Month'],
        value_vars=['Long Positions', 'Short Positions'],
        var_name='Position',
        value_name='Contracts'
    )

    # Plot the chart
    cot_chart = (
        alt.Chart(melted_cot)
            .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
            .encode(
                x=alt.X('Month:N', title='Month', axis=alt.Axis(labelAngle=-45)),
                y=alt.Y('Contracts:Q', title='Number of Contracts', stack='zero'),
                color=alt.Color(
                    'Position:N',
                    scale=alt.Scale(domain=['Long Positions', 'Short Positions'], range=['#1f77b4', '#ff7f0e']),
                    legend=alt.Legend(title="Position")
                ),
                tooltip=['Month', 'Position', 'Contracts']
            )
            .properties(
                width=700,
                height=400,
                title=f'COT Long vs Short Positions for {selected_pair}'
            )
    )

    st.altair_chart(cot_chart, use_container_width=True)

