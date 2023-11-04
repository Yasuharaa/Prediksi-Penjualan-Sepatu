import pickle
import streamlit as st


model = pickle.load(open('model.sav', 'rb'))

st.tittle('Prediksi Penjualan Sepatu berdasarkan Minat Pembeli')

minat = st.number_input('Minat')

prediksi = ''

if st.button('Prediksi Penjualan'):
    prediksi = model.predict(minat)
    st.write('Predikasi Penjualan Sepatu adalah : ', prediksi)
