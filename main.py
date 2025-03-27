from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Uygulama oluştur
app = FastAPI()

# Upload Model
model = joblib.load("xgboost_model.pkl")


# Input Data Model
class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity_INLAND: int
    ocean_proximity_NEAR_BAY: int
    ocean_proximity_NEAR_OCEAN: int
    rooms_per_household: float


@app.get("/")
def read_root():
    return {"message": "House Price Prediction API is running "}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Veriyi numpy array'e çevir
    data = np.array([[features.longitude, features.latitude,
                      features.housing_median_age, features.total_rooms,
                      features.total_bedrooms, features.population,
                      features.households, features.median_income,
                      features.ocean_proximity_INLAND,
                      features.ocean_proximity_NEAR_BAY,
                      features.ocean_proximity_NEAR_OCEAN,
                      features.rooms_per_household]])

    # Predict
    prediction = model.predict(data)
    return {"predicted_price": round(float(prediction[0]), 2)}
