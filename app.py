import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model_prediksi.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Prediksi Hasil Produksi Padi")  # Mengganti judul

# Informasi Akurasi Model
st.markdown("**Model ini memiliki akurasi sebesar 93,54% dalam memprediksi hasil produksi padi.**")

# Luas Panen dengan batasan minimal dan maksimal, dan satuan hektar
Luas_panen = st.number_input("Luas Panen (hektar) (min: 0, maks: 1000000) ", min_value=0.0, max_value=1000000.0, format="%.2f")
# Curah Hujan dengan satuan mm
Curah_hujan = st.number_input("Curah hujan (mm) (min: 0, maks: 5000) ", min_value=0.0, max_value=5000.0, format="%.2f")
# Kelembapan dengan satuan persen
Kelembapan = st.number_input("Kelembapan (%) (min: 0, maks: 100) ", min_value=0.0, max_value=100.0, format="%.2f")
# Suhu Rata-rata dengan satuan derajat Celsius
Suhu_ratarata = st.number_input("Suhu rata-rata (°C) (maks: 100) ", max_value=100.0, format="%.2f")

if st.button("Prediksi"):
    features = np.array([[Luas_panen, Curah_hujan, Kelembapan, Suhu_ratarata]])
    prediction = model.predict(features)
    st.write(f"Produksi Padi yang Diprediksi: {prediction[0]:.2f} ton")


