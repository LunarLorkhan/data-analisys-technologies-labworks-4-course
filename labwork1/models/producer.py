from sqlalchemy import Column, String

from .base import BaseIdModel


class Producer(BaseIdModel):
    """Producer model."""
    __tablename__ = "producer"

    name = Column(String(length=256), nullable=False)
    description = Column(String(length=2048))
    address = Column(String(length=256), nullable=False)
