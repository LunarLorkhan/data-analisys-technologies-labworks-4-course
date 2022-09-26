from sqlalchemy import Column, String

from .base import BaseIdModel


class Seller(BaseIdModel):
    """Seller model."""
    __tablename__ = "seller"

    name = Column(String(length=256), nullable=False)
