from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base, BaseIdModel


class OrderProduct(BaseIdModel):
    """Intermediate model between order and product."""
    __tablename__ = 'orderproduct'

    amount = Column(Integer, default=1, nullable=False)

    product_id = Column(ForeignKey('product.id'))
    order_id = Column(ForeignKey('order.id'))

    products = relationship('Product')
    orders = relationship('Order')
