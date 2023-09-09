import logging

import pandas as pd
import streamlit as st

logging.getLogger("streamlit_searchbox").setLevel(logging.DEBUG)
data = pd.read_csv('supermarket_train.csv', delimiter=';')['name'].unique()
st.set_page_config(page_title='Формирование чека', layout="wide", initial_sidebar_state="auto", page_icon="📖")

import requests



st.header = "Поиск по документации"
state = st.session_state



if 'ITEMS' not in state:
    state.ITEMS = []





st.markdown("---")

def _set_items():
    state.ITEMS = state.item_choice
    print(state.item_choice)
    if(state.ITEMS == ['1']):
        st.subheader('LOL')
    else:
        st.subheader('NOT LOL')


st.multiselect('Выберите позиции', options=data, default=[], on_change=_set_items, key='item_choice')



def main():
    st.title = "Формирование чека"

if __name__ == '__main__':
    main()