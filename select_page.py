import streamlit as st
from intro_screen import intro_screen
from factors import factors
from top import top


def select_page():
    page = st.sidebar.selectbox("Выбрать страницу",
                                ["Общая информация",
                                 'Факторы благополучия',
                                 'Топ благополучных микрорайонов'
                                 ])

    if page == "Общая информация":
        intro_screen()
    elif page == 'Факторы благополучия':
        factors()
    elif page == 'Топ благополучных микрорайонов':
        top()
