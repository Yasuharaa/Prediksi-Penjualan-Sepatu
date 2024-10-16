import pickle
import streamlit as st
import numpy as np

# Load model.sav
try:
    model = pickle.load(open('model.sav', 'rb'))
except FileNotFoundError:
    st.error("Model tidak ditemukan")
    st.stop()

st.title('Prediksi Penjualan Sepatu berdasarkan Minat Pembeli di Toko Bambang')

# Input minat
input_minat = st.number_input('Minat Pembeli', value=0, step=1)
minat = np.array([[input_minat]])

input_ukuran = st.number_input('Ukuran Sepatu', value=0, step=1)
ukuran = np.array([[input_minat]])

# Button Prediksi
if st.button('Prediksi Penjualan'):
    st.write('Jika minat pembeli terhadap suatu merek Sepatu : ', input_minat)

    # Buat prediksi dari inputan minat berdasarkan model
    try:
        prediksi = model.predict(minat)
        prediksi_int = int(prediksi[0])
        st.write('Prediksi Penjualan Sepatu adalah : ')
        st.success(prediksi_int + ukuran)
    except Exception as e:
        st.error(f"An error occurred during prediction: {str(e)}")
