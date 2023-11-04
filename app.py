import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

model = pickle.load(open('model.sav', 'rb'))

st.title('Prediksi Penjualan Sepatu berdasarkan Minat Pembeli')

input = st.number_input('Minat')
minat = np.array([[input]])


if st.button('Prediksi Penjualan'):
    st.write('Jika minat pembeli terhadap suatu merek Sepatu : ', input)
    prediksi = model.predict(minat)
    st.write('Predikasi Penjualan Sepatu adalah : ')
    st.success(prediksi)