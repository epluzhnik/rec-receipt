import uvicorn
from fastapi import FastAPI

from app.src.models import ItemRecommendationRequest, ItemRecommendationResponse

app = FastAPI()


@app.post("/recommendation")
async def read_root(request: ItemRecommendationRequest) -> ItemRecommendationResponse:

    return ItemRecommendationResponse(item="candidates")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)