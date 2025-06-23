import streamlit as st
from intro_screen import intro_screen


def select_page():
    page = st.sidebar.selectbox("Выбрать страницу",
                                ["Общая информация",
                                 ])

    if page == "Общая информация":
        intro_screen()
