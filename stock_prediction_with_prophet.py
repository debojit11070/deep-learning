import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from prophet import Prophet

st.header('Stock Market Predictor')

# Input stock symbol and date range
stock = st.text_input('Enter Stock Symbol', 'GOOG')
start = '2012-01-01'
end = '2022-12-31'

# Download stock data
data = yf.download(stock, start, end)

# Display stock data
st.subheader('Stock Data')
st.write(data)

# Prepare data for Prophet
df = data[['Close']].reset_index()
df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)

# Split the data into training and testing sets
train_data = df.iloc[:int(len(df) * 0.80)]
test_data = df.iloc[int(len(df) * 0.80):]

# Initialize and train the Prophet model
model = Prophet()
model.fit(train_data)

# Forecasting without caching
def make_forecast(_model, periods):
    future = _model.make_future_dataframe(periods=periods)
    forecast = _model.predict(future)
    return forecast

# Call the function to make predictions
forecast = make_forecast(model, len(test_data))

# Plotting the forecast
st.subheader('Price vs MA50')
ma_50_days = data.Close.rolling(50).mean()
fig1 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig1)

st.subheader('Price vs MA50 vs MA100')
ma_100_days = data.Close.rolling(100).mean()
fig2 = plt.figure(figsize=(8, 6))
plt.plot(ma_50_days, 'r')
plt.plot(ma_100_days, 'b')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig2)

st.subheader('Price vs MA100 vs MA200')
ma_200_days = data.Close.rolling(200).mean()
fig3 = plt.figure(figsize=(8, 6))
plt.plot(ma_100_days, 'r')
plt.plot(ma_200_days, 'b')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig3)

# Plot original and predicted prices
st.subheader('Original Price vs Predicted Price')
fig4 = plt.figure(figsize=(8, 6))
plt.plot(test_data['ds'], test_data['y'], 'g', label='Original Price')
plt.plot(forecast['ds'], forecast['yhat'], 'r', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()
st.pyplot(fig4)

# Show the forecast components
st.subheader('Forecast Components')
fig5 = model.plot_components(forecast)
st.pyplot(fig5)
