from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=256))
    price = Column(Integer)
    description = Column(String(length=65536))
    amount = Column(Integer)


class Seller(Base):
    __tablename__ = "seller"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    name = Column(String(length=256))


if __name__ == '__main__':
    from engine import engine
    Base.metadata.create_all(engine)
