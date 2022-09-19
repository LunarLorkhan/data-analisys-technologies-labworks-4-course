from sqlalchemy import Column, String

from .base import BaseIdModel


class Category(BaseIdModel):
    """Category model for product."""
    __tablename__ = 'category'

    name = Column(String(length=256), nullable=False)
    description = Column(String(length=2048))
