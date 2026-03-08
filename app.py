import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Боловсрол ба Хөдөлмөр эрхлэлт", layout="wide", page_icon="📊")

st.title("📊 Боловсрол ба Хөдөлмөр эрхлэлт – Интерактив шинжилгээ (АХС 2023)")
st.subheader("СЭЗИС оюутан Telmen Oti")

col1, col2, col3 = st.columns(3)
col1.metric("Rows (ажиглалт)", "30,443")
col2.metric("Columns", "7")
col3.metric("Workforce Rate", "63.5%")   # ← чиний засварласан тоо

c1, c2 = st.columns(2)
with c1:
    years = st.slider("Суралцсан жил", 0, 21, 12)
    age = st.slider("Нас", 15, 64, 30)
    female = st.checkbox("Эмэгтэй")
with c2:
    urban = st.checkbox("Хот/Аймгийн төвд амьдардаг")
    married = st.checkbox("Гэрлэсэн")
    disability = st.checkbox("Хөгжлийн бэрхшээлтэй")

const = -7.6612
coef = {'years_school': 0.0503, 'a05': 0.4674, 'age_sq': -0.0057,
        'female': -0.8070, 'urban': -1.1124, 'married': 0.3356, 'disability': -0.5574}

linear = const + coef['years_school']*years + coef['a05']*age + coef['age_sq']*(age**2) + \
         coef['female']*int(female) + coef['urban']*int(urban) + coef['married']*int(married) + coef['disability']*int(disability)

prob = 1 / (1 + np.exp(-linear))
st.success(f"**Хөдөлмөр эрхлэх магадлал: {prob*100:.1f}%**")
