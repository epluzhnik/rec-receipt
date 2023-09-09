from pydantic import BaseModel
from typing import List

class ItemRecommendationRequest(BaseModel):
    items: List[int]
    device_id: int

class ItemRecommendationResponse(BaseModel):
    items: List[int]