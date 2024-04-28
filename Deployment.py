import streamlit as st
import yfinance as yf
import pandas as pd

df = pd.read_csv('TESLA.csv')

st.write("""
# Tesla Stock Price Research

The below charts will show the stock price of Tesla from 2021-09-29 to 2022-09-29.
Please enter a date to search the stock price. 
""")

# Fetch Tesla stock data
tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2021-09-29', end='2022-09-29')

# Display date input
start_date = st.date_input("Start Date", value=pd.to_datetime("2021-09-29"))
end_date = st.date_input("End Date", value=pd.to_datetime("2022-09-29"))

# Filter the data based on selected dates
filtered_data = tickerDf.loc[start_date:end_date]

# Display filtered data as table
st.table(filtered_data)

# Display charts for Open, High, Low, Close, Adj Close, and Volume
st.write("""
## Open
""")
st.bar_chart(filtered_data['Open'])

st.write("""
## High
""")
st.bar_chart(filtered_data['High'])

st.write("""
## Low
""")
st.bar_chart(filtered_data['Low'])

st.write("""
## Close
""")
st.bar_chart(filtered_data['Close'])

st.write("""
## Adj Close
""")
st.bar_chart(filtered_data['Adj Close'])

st.write("""
## Volume
""")
st.bar_chart(filtered_data['Volume'])
