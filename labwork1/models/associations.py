from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base, BaseIdModel


class OrderProductAssociation(BaseIdModel):
    __tablename__ = 'orderproduct'

    amount = Column(Integer, default=1, nullable=False)

    product_id = Column(ForeignKey('product.id'))
    order_id = Column(ForeignKey('order.id'))

    products = relationship('Product')
    orders = relationship('Order')


class ProductWarehouseAssociation(Base):
    __tablename__ = 'productwarehouse'

    warehouse_id = Column(ForeignKey('warehouse.id'), primary_key=True)
    product_id = Column(ForeignKey('product.id'), primary_key=True)

    warehouses = relationship('Warehouse')
    products = relationship('Product')


class CategoryProductAssociation(Base):
    __tablename__ = 'categoryproduct'

    category_id = Column(ForeignKey('product.id'), primary_key=True)
    product_id = Column(ForeignKey('category.id'), primary_key=True)

    categories = relationship('Category')
    products = relationship('Product')
