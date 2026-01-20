# app.py
import streamlit as st
import pandas as pd
import joblib



model = joblib.load("best_model.pkl")

st.title(" Smartphone_Price_Predictor")

st.write("Enter smartphone features:")

ram = st.slider("RAM (GB)", 1, 16, 4)
rom = st.slider("Storage (GB)", 8, 512, 64)
battery = st.slider("Battery (mAh)", 1000, 6000, 3000)
camera = st.slider("Camera (MP)", 2, 108, 12)

# Add other inputs as needed

if st.button("Predict Price"):
    input_df = pd.DataFrame([[ram, rom, battery, camera]], columns=["RAM", "ROM", "Battery", "Camera"])
    st.write("Predicted Price: Rs.", round(model.predict(input_df)[0], 2))
