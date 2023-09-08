from pydantic import BaseModel


class ItemRecommendationRequest(BaseModel):
    items: [str]

class ItemRecommendationResponse(BaseModel):
    item: str