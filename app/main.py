from tqdm import tqdm
import json
import uvicorn
import numpy as np
import pandas as pd

from fastapi import FastAPI
from scipy import sparse as sps

from app.src.models import ItemRecommendationRequest, ItemRecommendationResponse, TrainDataset
from app.src.predictor import Predictor


app = FastAPI()
predictor = Predictor('sample.json')


def fit_model(data, reg_weight=10):
    G = data.T @ data
    G += reg_weight * sps.identity(G.shape[0])
    P = np.linalg.inv(G.todense())
    model = P / (-np.diag(P))
    np.fill_diagonal(model, 0.)
    
    return model

def get_ease(df):

    user2idx = {v: k for k, v in enumerate(df.receipt_id.unique())}
    item2idx = {v: k for k, v in enumerate(df.item_id.unique())}

    idx2user = {k:v for v, k in user2idx.items()}
    idx2item = {k:v for v, k in item2idx.items()}

    df['user_id'] = df.receipt_id.apply(lambda x: user2idx[x])
    df['item_id'] = df.item_id.apply(lambda x: item2idx[x])
    
    matrix = sps.coo_matrix(
        (np.ones(df.shape[0]), (df['user_id'], df['item_id'])),
        shape=(len(user2idx), len(item2idx)),
    )
    

    w1 = fit_model(matrix)

    return user2idx, item2idx, idx2item,  w1


@app.post("/recommendation")
async def recommendation(request: ItemRecommendationRequest):
    result = predictor.get_recommendations(list_of_items=request.items, device_id=request.device_id)
    return ItemRecommendationResponse(items=result)


@app.post("/train_model")
async def train_model(request: TrainDataset, new_file_name = 'new_sample.json'):
    global_matrix = {}

    df = pd.read_json(request.dataset, orient ='index')
    for dev in df.device_id.unique():
        tt  = df.loc[df.device_id==dev].copy()
        _, item2idx, _,  w = get_ease(tt)
        global_matrix[int(dev)] = {'item2idx': item2idx, 'w': w.tolist()}
        
    global_matrix_cleaned = {}
    for nn, dev in tqdm(enumerate(global_matrix.keys())):
        print(f"{nn} из {len(global_matrix.keys())}")
        nd = {}
        nd['item2idx'] = {int(x): int(y) for x, y in global_matrix[dev]['item2idx'].items()}
        nd['w'] = global_matrix[dev]['w']
        
        global_matrix_cleaned[dev] = nd

    with open(new_file_name,'w') as f:
        json.dump(global_matrix_cleaned, f)   

    predictor.change_model(new_file_name)
    return 200


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)   