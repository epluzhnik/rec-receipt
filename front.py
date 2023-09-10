import logging
import requests
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
title_ = st.empty()
title_.title('Универсальная рекомендательная система. Команда Link Bizkitыы')
uploaded_file = st.file_uploader("Загрузите тренировочный датасет:")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep='\t')
    requests.post('https://a20391-b090.s.d-f.pw/train_model', json={"dataset":df.to_json( orient="index")})



def filter_names():
    print("change names")
    state.NAMES  = data.loc[data['device_id'] == device_id]['name'].unique()
    print(len(data.loc[data['device_id'] == device_id]['name'].unique()))


col1, col2, = st.columns(2)
#
with col1:
    device_id = st.selectbox(
        'Идентификатор кассы',
        device_ids,
        on_change = filter_names)
    col1_2 = st.empty()





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
        "https://a20391-b090.s.d-f.pw/recommendation",
        timeout=15,
        json={"items": items, "device_id": int(device_id)}
    ).json()

    print(response)

    with col2:
        st.subheader(itemIdToName[response['items'][0]])


col1_2.multiselect('Выберите позиции', options=state.NAMES, default=[], on_change=_set_items, key='item_choice')

def main():
    st.title = "Формирование чека"

if __name__ == '__main__':
    main()