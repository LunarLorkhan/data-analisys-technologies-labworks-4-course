import enum

from sqlalchemy import Column, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import BaseIdModel


class OrderStatusEnum(enum.Enum):
    """Statuses of order."""
    performed = 'performed'
    cancelled = 'cancelled'
    in_process = 'in process'


class Order(BaseIdModel):
    """Order model.

    Contains foreign key on Shop and Warehouse models.

    """
    __tablename__ = 'order'

    status = Column(Enum(OrderStatusEnum))
    datetime = Column(DateTime)
    # Foreign keys
    shop_id = Column(ForeignKey('shop.id'))

    shop = relationship('Shop', back_populates='orders')
