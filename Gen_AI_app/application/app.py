# application/app.py

import streamlit as st
import requests

st.title('Gen AI App')

input_data = st.text_input('Enter input data (comma-separated)')

if st.button('Predict'):
    input_list = list(map(float, input_data.split(',')))
    response = requests.post('http://localhost:5000/predict', json={'input': input_list})
    prediction = response.json()['prediction']
    st.write(f'Prediction: {prediction}')
