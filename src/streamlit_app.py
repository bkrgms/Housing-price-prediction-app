import streamlit as st
import joblib
import pandas as pd


model = joblib.load('eniyi.joblib')  


st.title('Ev Fiyat Tahmin Uygulaması')


st.header('Ev Özelliklerini Girin')

oda_sayisi = st.slider('Oda Sayısı', 1, 5, 3)
metrekare = st.number_input('Metrekare', min_value=50, max_value=200, value=100)
ev_yasi = st.slider('Ev Yaşı (Yıl)', 0, 30, 10)
lokasyon = st.selectbox('Lokasyon', ['Mahalle_A', 'Mahalle_B', 'Mahalle_C', 'Mahalle_D'])


lokasyon_map = {'Mahalle_A': 0, 'Mahalle_B': 1, 'Mahalle_C': 2, 'Mahalle_D': 3}
lokasyon_encoded = lokasyon_map[lokasyon]


input_data = pd.DataFrame({
    'Oda Sayısı': [oda_sayisi],
    'Metrekare': [metrekare],
    'Ev Yaşı': [ev_yasi],
    'Lokasyon': [lokasyon_encoded]
})


if st.button('Fiyatı Tahmin Et'):

    predicted_price = model.predict(input_data) 
    

    st.write(f'Tahmin Edilen Ev Fiyatı: {predicted_price[0]:.2f} TL')
