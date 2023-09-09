import uvicorn
from fastapi import FastAPI

from app.src.models import ItemRecommendationRequest, ItemRecommendationResponse
from app.src.predictor import Predictor

app = FastAPI()

predictor = Predictor()

@app.post("/recommendation")
async def recommendation(request: ItemRecommendationRequest):
    result = predictor.get_recommendations(list_of_items=request.items, device_id=request.device_id)
    return ItemRecommendationResponse(items=result)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)