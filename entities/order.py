from datetime import datetime
from pydantic import BaseModel,Field

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class Item(BaseModel):
    product_id: str
    bought_quantity: int = Field(gt=0)

class Order(BaseModel):
    created_at: datetime
    items: list[Item]
    total_amount: float = Field(gt=0)
    user_address: UserAddress

def order_serializer(order):
    return { 
            "id": str(order.get('_id')),
            "items": list(order.get('items')),
            "total_amount": float(order.get("total_amount")),
            "user_address": dict(order.get('user_address'))
    }