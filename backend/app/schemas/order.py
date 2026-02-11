from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    status: str
    total_amount: float
    created_at: datetime
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True
