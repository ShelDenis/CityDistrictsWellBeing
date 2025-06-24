import streamlit as st
from intro_screen import intro_screen
from factors import factors
from top import top
from prediction import prediction


def select_page():
    page = st.sidebar.selectbox("Выбрать страницу",
                                ["Общая информация",
                                 'Факторы благополучия',
                                 'Топ благополучных микрорайонов',
                                 'Предсказать благополучие'
                                 ])

    if page == "Общая информация":
        intro_screen()
    elif page == 'Факторы благополучия':
        factors()
    elif page == 'Топ благополучных микрорайонов':
        top()
    elif page == 'Предсказать благополучие':
        prediction()
