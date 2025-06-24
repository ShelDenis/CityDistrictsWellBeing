import streamlit as st
import pandas as pd
from load_data import load_data
from traslit import translit, get_okrug


colors = {
    9: '7ffa94',
    8: '7ffa94',
    7: 'f9ff80',
    6: 'f9ff80',
    5: 'ff793b',
    4: 'ff793b',
    3: 'ff3b3b',
    2: 'ff3b3b',
    1: 'ff3b3b',
}


def top():
    data = load_data()

    st.header('Топ самых благополучных районов города Омска')

    top_data = data[['district_name', 'okrug', 'well_being']].sort_values('well_being', ascending=False)

    count = 1
    for index, row in top_data.iterrows():
        st.markdown(
            f"""
            <div style="background-color: #{colors[row['well_being'] // 10]}; padding: 10px; border-radius: 5px;">
                <p>{count}) {translit(row['district_name'])}
                 ({get_okrug(row['okrug'])}): <b>{row['well_being']}%</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )
        count += 1
