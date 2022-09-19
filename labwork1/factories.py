import factory
from factory.alchemy import SQLAlchemyModelFactory
from factory.fuzzy import FuzzyAttribute, FuzzyChoice, FuzzyInteger
from faker import Faker
from sqlalchemy.orm import scoped_session, sessionmaker

from engine import engine
from models import (
    Category,
    CategoryProductAssociation,
    Order,
    OrderProductAssociation,
    OrderStatusEnum,
    Producer,
    Product,
    ProductWarehouseAssociation,
    Seller,
    Shop,
    Warehouse,
)

fake = Faker()

session = scoped_session(sessionmaker(bind=engine))


class SellerFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Seller: {fake.company()}')

    class Meta:
        model = Seller
        sqlalchemy_session = session


class ProducerFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Producer: {fake.company()}')
    description = fake.text()
    address = fake.address()

    class Meta:
        model = Producer
        sqlalchemy_session = session


class ProductFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Product: {fake.name()}')
    price = FuzzyInteger(low=10000, high=1000000)
    description = fake.text()
    amount = FuzzyInteger(low=0, high=100)

    producer = factory.SubFactory(ProducerFactory)
    seller = factory.SubFactory(SellerFactory)

    class Meta:
        model = Product
        sqlalchemy_session = session


class CategoryFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Category: {fake.name()}')
    description = fake.text()

    class Meta:
        model = Category
        sqlalchemy_session = session


class WarehouseFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Warehouse: {fake.company()}')
    address = fake.address()

    class Meta:
        model = Warehouse
        sqlalchemy_session = session


class CategoryProductFactory(SQLAlchemyModelFactory):
    categories = factory.SubFactory(CategoryFactory)
    products = factory.SubFactory(ProductFactory)

    class Meta:
        model = CategoryProductAssociation
        sqlalchemy_session = session


class ProductWarehouseFactory(SQLAlchemyModelFactory):
    products = factory.SubFactory(ProductFactory)
    warehouses = factory.SubFactory(WarehouseFactory)

    class Meta:
        model = ProductWarehouseAssociation
        sqlalchemy_session = session


class ShopFactory(SQLAlchemyModelFactory):
    name = FuzzyAttribute(lambda: f'Shop: {fake.company()}')
    address = fake.address()

    class Meta:
        model = Shop
        sqlalchemy_session = session


class OrderFactory(SQLAlchemyModelFactory):
    status = FuzzyChoice(choices=OrderStatusEnum)
    shop = factory.SubFactory(ShopFactory)
    warehouse = factory.SubFactory(WarehouseFactory)

    class Meta:
        model = Order
        sqlalchemy_session = session


class OrderProductFactory(SQLAlchemyModelFactory):
    orders = factory.SubFactory(OrderFactory)
    products = factory.SubFactory(ProductFactory)
    amount = FuzzyInteger(low=10000, high=1000000)

    class Meta:
        model = OrderProductAssociation
        sqlalchemy_session = session
