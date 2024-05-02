import streamlit as st
import pandas as pd

df = pd.read_csv('TESLA.csv')

df['Date'] = pd.to_datetime(df['Date'])

st.title("Tesla Stock Price App")
st.write("""
The below charts will show the stock price of Tesla from 2021-09-29 to 2022-09-29.
Please enter a date to search the stock price. 
""")

start_date = st.date_input("Start Date", value=pd.Timestamp("2021-09-29"))
end_date = st.date_input("End Date", value=pd.Timestamp("2022-09-29"))

start_date = pd.Timestamp(start_date)
end_date = pd.Timestamp(end_date)

if st.button('Submit'):
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    st.subheader(f"Stock Price Data\n Stock Price Details from {start_date} to {end_date}")
    st.write(filtered_data)


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
