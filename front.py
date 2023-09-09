import logging

import pandas as pd
import streamlit as st

logging.getLogger("streamlit_searchbox").setLevel(logging.DEBUG)
data = pd.read_csv('supermarket_train.csv', delimiter=';')
device_ids = data['device_id'].unique()
filtered = data.loc[data['device_id'] == 352398080391651]
names = filtered['name'].unique()
nameToItemId = dict(zip(data.name, data.item_id))
itemIdToName = dict(zip(data.item_id, data.name))
st.set_page_config(page_title='Формирование чека', layout="wide", initial_sidebar_state="auto", page_icon="📖")

import requests

def filter_names():
    print("change names")
    state.NAMES  = data.loc[data['device_id'] == device_id]['name'].unique()
    print(len(data.loc[data['device_id'] == device_id]['name'].unique()))

device_id = st.selectbox(
    'Идентификатор кассы',
    device_ids,
    on_change = filter_names)



st.header = "Поиск по документации"
state = st.session_state



if 'ITEMS' not in state:
    state.ITEMS = []
    state.NAMES = data.loc[data['device_id'] == device_id]['name'].unique()


st.markdown("---")

def _set_items():
    state.ITEMS = state.item_choice
    items =[]
    for item in state.item_choice:
        items.append(nameToItemId[item])
    print(items)
    print(state.item_choice)
    print(device_id)
    response = requests.post(
        "http://0.0.0.0:8000/recommendation",
        timeout=15,
        json={"items": items, "device_id": int(device_id)}
    ).json()
    print(response)

    st.subheader(itemIdToName[response['items'][0]])



st.multiselect('Выберите позиции', options=state.NAMES, default=[], on_change=_set_items, key='item_choice')



def main():
    st.title = "Формирование чека"

if __name__ == '__main__':
    main()