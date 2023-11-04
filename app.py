import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics

model = pickle.load(open('model.sav', 'rb'))

st.tittle('Prediksi Penjualan Sepatu berdasarkan Minat Pembeli')

minat = st.number_input('Minat')

prediksi = ''

if st.button('Prediksi Penjualan'):
    prediksi = model.predict(minat)
    st.write('Predikasi Penjualan Sepatu adalah : ', prediksi)
