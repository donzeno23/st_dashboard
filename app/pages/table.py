import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

@st.cache_data()
def load_data():
    data = pd.read_csv('./data/data.csv', parse_dates=['referenceDate'])
    return data

data = load_data()

AgGrid(data, height=400)
