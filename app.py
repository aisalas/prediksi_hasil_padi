import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_prediksi.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Prediksi Produksi Padi")

Luas_panen = st.number_input("Luas Panen")
Curah_hujan = st.number_input("Curah hujan")
Kelembapan = st.number_input("Kelembapan")
Suhu_ratarata = st.number_input("Suhu rata-rata")

if st.button("Prediksi"):
    features = np.array([[Luas_panen, Curah_hujan, Kelembapan, Suhu_ratarata]])
    prediction = model.predict(features)
    st.write(f"Produksi Padi yang Diprediksi: {prediction[0]:.2f}")

