from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseIdModel


class Shop(BaseIdModel):
    __tablename__ = 'shop'

    name = Column(String(length=256), nullable=False)
    address = Column(String(length=256), nullable=False)

    orders = relationship('Order', back_populates='shop')
