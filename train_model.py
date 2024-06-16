import pandas as pd
from xgboost import XGBRegressor
import joblib

# Load the dataset
df = pd.read_csv('TESLA.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Prepare the data
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

X = df.drop(['Close', 'Date'], axis=1).values
y = df['Close'].values

# Train the model
model = XGBRegressor()
model.fit(X, y)

# Save the model
joblib.dump(model, 'tesla_stock_model.pkl')
