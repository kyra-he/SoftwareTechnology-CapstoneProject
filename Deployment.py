import streamlit as st
import pandas as pd
import csv
import numpy as np

with open('TESLA.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

# Title and Description
st.title("Tesla Stock Price App")
st.write("""
The below charts will show the stock price of Tesla from 2021-09-29 to 2022-09-29.
Please enter a date to search the stock price. 
""")

# Display date input
start_date = st.date_input("Start Date", value=pd.to_datetime("2021-09-29"))
end_date = st.date_input("End Date", value=pd.to_datetime("2022-09-29"))

# Filter the data based on selected dates
filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

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
