from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, unique=True, index=True, nullable=False)

    price = Column(Float, nullable=False)
    bulk_price = Column(Float, nullable=True)
    min_order_quantity = Column(Integer, default=1)

    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
