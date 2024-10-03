# code/deployment/api/main.py
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model
model = joblib.load("models/model.pkl")
app = FastAPI()

# Define the request body
class IrisRequest(BaseModel):
    carat: float
    color: int
    Length: float
    Width: float

@app.post("/predict")
def predict_iris(data: IrisRequest):
    features = np.array([[data.carat, data.color, data.Length, data.Width]])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
