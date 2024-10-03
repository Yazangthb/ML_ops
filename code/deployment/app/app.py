# code/deployment/app/app.py
import streamlit as st
import requests

st.title("diamond price Prediction")

carat = st.number_input("carat", min_value=0.0, max_value=10.0, value=1.0)
color = st.number_input("color", min_value=0, max_value=6, value=1)
Length = st.number_input("Length", min_value=0.0, max_value=100.0, value=5.0)
Width = st.number_input("Width", min_value=0.0, max_value=100.0, value=5.0)

if st.button("Predict"):
    response = requests.post("http://backend:8001/predict", json={
        "carat": carat,
        "color": color,
        "Length": Length,
        "Width": Width
    })
    
    prediction = response.json()
    st.write(f"answer is {prediction['prediction']}")
    # st.write(f"Prediction: Iris class {prediction['prediction']}")
