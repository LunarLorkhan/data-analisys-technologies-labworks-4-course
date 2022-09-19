from sqlalchemy import Column, String

from .base import BaseIdModel


class Warehouse(BaseIdModel):
    """Warehouse model."""
    __tablename__ = 'warehouse'

    name = Column(String(length=256), nullable=False)
    address = Column(String(length=256), nullable=False)
