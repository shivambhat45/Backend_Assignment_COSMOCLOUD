from pydantic import BaseModel,Field


class Product(BaseModel):
    name: str
    price: float
    quantity: int = Field(gt=0)


def product_serializer(product):
    return {
        "id": str(product.get('_id')),
        "name": str(product.get('name')),
        "price": product.get('price'),
        "quantity": int(product.get('quantity'))
    }