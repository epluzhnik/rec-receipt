import json

import numpy as np

class Predictor:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self._model = json.load(f)

    def get_recommendations(self, list_of_items, device_id):
        device_id = str(device_id)

        if device_id not in self._model:
            raise ValueError('no such device id')

        particular_model = self._model[device_id]

        item2idx = particular_model['item2idx']
        num_of_items = len(item2idx)

        encoded_items = [item2idx[str(x)] for x in list_of_items if str(x) in item2idx]
        if len(encoded_items) == 0:
            encoded_items = [0]

        vector = np.zeros(num_of_items)
        vector[encoded_items] = 1

        predictions = vector.dot(particular_model['w'])
        predictions[vector == 1] = -np.inf
        items = np.argsort(-predictions)[:10]

        idx2item = {k: v for v, k in item2idx.items()}

        decoded = [idx2item[x] for x in items]

        return decoded
    
    def change_model(self, new_f_path):
        with open(new_f_path, 'r') as f:
            self._model = json.load(f)
