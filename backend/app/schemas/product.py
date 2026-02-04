from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    bulk_price: float | None = None
    min_order_quantity: int = 1
    stock: int = 0
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
