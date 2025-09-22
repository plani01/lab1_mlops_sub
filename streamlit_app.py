import streamlit as st
import requests
import os

st.title('MPG Prediction For Cars')

cylinders = st.number_input('Cylinders', min_value=0.0, max_value=100.0, step=1.0, value=0.0)
displacement = st.number_input('Displacement', min_value=0.0, max_value=1000.0, step=10.0, value=0.0)
horsepower = st.number_input('Horsepower', min_value=0.0, max_value=1000.0, step=10.0, value=0.0)
weight = st.number_input('Weight', min_value=0.0, max_value=10000.0, step=100.0, value=0.0)
acceleration = st.number_input('Acceleration', min_value=0.0, max_value=100.0, step=1.0, value=0.0)
model_year = st.number_input('Model Year', min_value=70.0, max_value=100.0, step=1.0, value=70.0)
origin = st.number_input('Origin', min_value=0.0, max_value=3.0, step=1.0, value=0.0)

if st.button('Predict'):
    data = {
        'cylinders': cylinders,
        'displacement': displacement,
        'horsepower': horsepower,
        'weight': weight,
        'acceleration' : acceleration,
        'model_year' : model_year,
        'origin' : origin
    }

    try:
        response = requests.post('https://iris-app-117339455766.us-east4.run.app/predict', json=data)
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.success(f'Predicted MPG: {prediction}')
        else:
            st.error(f'Error occurred during prediction. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        st.error(f'Error occurred during prediction: {str(e)}')
