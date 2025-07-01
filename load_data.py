import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    data = pd.read_csv('data/districts.csv', encoding='utf-8', delimiter=',')
    # data.drop(['Unnamed: 0'], axis=1, inplace=True)
    return data
