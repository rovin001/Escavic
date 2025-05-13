# import pandas as pd
# import streamlit as st

# def show_fundamentals():
#     st.subheader("📉 Inflation Rate (CPI)")
#     df = pd.read_csv("data/cpi_data.csv")
#     df['Date'] = pd.to_datetime(df['Date'])
#     st.line_chart(df.set_index('Date')['InflationRate'])

# def show_gdp_chart():
#     st.subheader("GDP Growth Rate Over Time")
#     df = pd.read_csv('data/gdp_data.csv')
#     df['Date'] = pd.to_datetime(df['Date'])
#     st.line_chart(df.set_index('Date')['GDP Growth Rate (%)'])

# def show_pmi_chart():
#     st.subheader("PMI Index Over Time")
#     df = pd.read_csv('data/pmi_data.csv')
#     df['Date'] = pd.to_datetime(df['Date'])
#     st.line_chart(df.set_index('Date')['PMI Index'])

# def show_interest_rate_chart():
#     st.subheader("Interest Rate Over Time")
#     df = pd.read_csv('data/interest_rate_data.csv')
#     df['Date'] = pd.to_datetime(df['Date'])
#     st.line_chart(df.set_index('Date')['Interest Rate (%)'])
import streamlit as st
import pandas as pd
import os

def show_fundamentals():
    st.subheader("📊 Fundamental Data by Currency")

    # Step 1: Get available currencies from folder names
    base_path = "data/fundamental_data"
    currencies = [folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]

    # Step 2: Select currency
    selected_currency = st.selectbox("Select a Currency", currencies)

    # Step 3: Select fundamental data type
    data_types = {
        "CPI": "cpi_data.csv",
        "GDP": "gdp_data.csv",
        "PMI": "pmi_data.csv",
        "Interest Rate": "interest_rate_data.csv"
    }

    selected_type = st.selectbox("Select Fundamental Data Type", list(data_types.keys()))
    file_name = data_types[selected_type]

    # Step 4: Load and show data
    file_path = os.path.join(base_path, selected_currency, file_name)

    try:
        df = pd.read_csv(file_path)

        # Sort by date descending if 'Date' column exists
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df = df.sort_values(by='Date', ascending=False)

        st.success(f"Loaded {selected_type} data for {selected_currency}")
        st.dataframe(df)

        # Optional: Plot
        if 'Date' in df.columns and df.columns[1] != 'Date':
            st.line_chart(df.set_index('Date')[df.columns[1]])

    except FileNotFoundError:
        st.error("Data file not found. Please check your folder structure.")
