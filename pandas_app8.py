import streamlit as st
import pandas as pd
from datetime import date

df = pd.read_csv("jeju_place.csv")

st.dataframe(df)

# [TODO] lat, lon이라는 컬럼에 위도, 경도 값을 담습니다.
df[["lat","lon"]] = df[["위도","경도"]]

# [TODO] 데이터 프레임을 단순히 st.map에 넘겨줍니다.
st.map(df)