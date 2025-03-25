import streamlit as st
import joblib
import numpy as np
import datetime

# Load trained model
model = joblib.load("xgboost_model.pkl")

# Title & Header
st.set_page_config(page_title="California House Price Predictor", layout="centered")
st.title("🏡 California House Price Prediction")
st.markdown("""
This application predicts the **median house value** in California based on housing data.

:information_source: **Note:**
- `Median Income` is scaled: **1 unit = $1,000**. So enter `4.5` for $4,500.
- Inputs should be within realistic California housing ranges.
""")

# Collect user input
st.subheader("Enter the features below:")

col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude", min_value=-125.0, max_value=-113.0, value=-118.0, step=0.01)
    housing_median_age = st.number_input("Median Age of House", min_value=1, max_value=100, value=30)
    total_rooms = st.number_input("Total Rooms", min_value=1, max_value=10000, value=5000)
    population = st.number_input("Population in Area", min_value=1, max_value=50000, value=1500)
    ocean_proximity_inland = st.radio("Is it INLAND?", [0, 1], index=1)

with col2:
    latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.2, step=0.01)
    total_bedrooms = st.number_input("Total Bedrooms", min_value=1, max_value=5000, value=1000)
    households = st.number_input("Number of Households", min_value=1, max_value=10000, value=500)
    median_income = st.number_input("Median Income (1 = $1,000)", min_value=0.0, max_value=20.0, value=4.5, step=0.1)
    rooms_per_household = st.number_input("Rooms per Household", min_value=0.0, max_value=50.0, value=10.0, step=0.1)

ocean_proximity_near_bay = st.checkbox("Is it NEAR BAY?")
ocean_proximity_near_ocean = st.checkbox("Is it NEAR OCEAN?")

# Prepare input for model
user_data = np.array([[
    longitude, latitude, housing_median_age, total_rooms,
    total_bedrooms, population, households, median_income,
    ocean_proximity_inland, int(ocean_proximity_near_bay),
    int(ocean_proximity_near_ocean), rooms_per_household
]])

# Store prediction history
if "history" not in st.session_state:
    st.session_state.history = []

# Predict
if st.button("Predict Price"):
    prediction = model.predict(user_data)
    result = round(prediction[0], 2)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"Estimated House Price: ${result:,.2f}")

    # Add to history
    st.session_state.history.append({
        "time": timestamp,
        "price": result,
        "input": user_data.tolist()[0]
    })

# Show prediction history
if st.session_state.history:
    st.subheader("📈 Prediction History")
    for item in reversed(st.session_state.history[-5:]):
        st.write(f"{item['time']} → ${item['price']:,.2f}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ by Levent Can | Powered by XGBoost & Streamlit")