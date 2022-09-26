from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseIdModel


class Product(BaseIdModel):
    """Product model."""
    __tablename__ = "product"

    name = Column(String(length=256), nullable=False)
    price = Column(Integer, nullable=True)
    description = Column(String(length=65536))
    amount = Column(Integer, nullable=False, default=0)

    seller_id = Column(Integer, ForeignKey('seller.id'))
    producer_id = Column(Integer, ForeignKey('producer.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    seller = relationship('Seller')
    producer = relationship('Producer')
    category = relationship('Category')
