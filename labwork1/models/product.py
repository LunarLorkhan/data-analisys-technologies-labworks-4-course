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

    seller = relationship('Seller', back_populates='product', uselist=False)
    producer = relationship('Producer', back_populates='product', uselist=False)


class Seller(BaseIdModel):
    """Seller model."""
    __tablename__ = "seller"

    name = Column(String(length=256), nullable=False)

    # Foreign keys
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='seller', uselist=False)


class Producer(BaseIdModel):
    """Producer model."""
    __tablename__ = "producer"

    name = Column(String(length=256), nullable=False)
    description = Column(String(length=2048))
    address = Column(String(length=256), nullable=False)

    # Foreign keys
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='producer', uselist=False)
