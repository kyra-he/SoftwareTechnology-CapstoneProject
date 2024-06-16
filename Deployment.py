import streamlit as st
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor
import os

# Load the dataset
df = pd.read_csv('TESLA.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Prepare the data
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

X = df.drop(['Close', 'Date'], axis=1).values
y = df['Close'].values

model_path = 'tesla_stock_model.pkl'

if not os.path.exists(model_path):
    st.write("Training the model as the model file does not exist...")
    # Train the model
    model = XGBRegressor()
    model.fit(X, y)
    # Save the model
    joblib.dump(model, model_path)
    st.write("Model trained and saved successfully.")
else:
    # Load the model
    model = joblib.load(model_path)
    st.write("Model loaded successfully.")

st.title("Tesla Stock Price Prediction App")
st.write("""
The below tool will allow you to input parameters to predict the future stock price of Tesla.
""")

# User input for prediction
year = st.number_input('Year', min_value=2021, max_value=2030, value=2023)
month = st.number_input('Month', min_value=1, max_value=12, value=1)
day = st.number_input('Day', min_value=1, max_value=31, value=1)
open_price = st.number_input('Open Price', min_value=0.0, value=700.0)
high_price = st.number_input('High Price', min_value=0.0, value=720.0)
low_price = st.number_input('Low Price', min_value=0.0, value=680.0)
adj_close_price = st.number_input('Adj Close Price', min_value=0.0, value=710.0)
volume = st.number_input('Volume', min_value=0, value=1000000)

# Create input DataFrame
input_data = pd.DataFrame({
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Adj Close': [adj_close_price],
    'Volume': [volume],
    'Year': [year],
    'Month': [month],
    'Day': [day]
})

# Predict the closing price
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f"The predicted closing price for Tesla on {year}-{month:02d}-{day:02d} is ${prediction[0]:.2f}")
