import factory
from factory.alchemy import SQLAlchemyModelFactory
from factory.fuzzy import FuzzyAttribute, FuzzyChoice, FuzzyInteger
from faker import Faker

from models import (Category, Order,
                    OrderStatusEnum, Producer,
                    Product, Seller, Shop, OrderProduct
                )
from session import session

fake = Faker()


class BaseFactory(SQLAlchemyModelFactory):
    id = factory.Sequence(lambda n: n)


class SellerFactory(BaseFactory):
    name = FuzzyAttribute(lambda: f'Seller: {fake.company()}')

    class Meta:
        model = Seller
        sqlalchemy_session = session


class ProducerFactory(BaseFactory):
    name = FuzzyAttribute(lambda: f'Producer: {fake.company()}')
    address = factory.Faker('address')

    class Meta:
        model = Producer
        sqlalchemy_session = session


class CategoryFactory(BaseFactory):
    name = FuzzyAttribute(lambda: f'Category: {fake.name()}')

    class Meta:
        model = Category
        sqlalchemy_session = session


class ProductFactory(BaseFactory):
    name = FuzzyAttribute(lambda: f'Product: {fake.name()}')
    price = FuzzyInteger(low=10000, high=1000000)
    amount = FuzzyInteger(low=0, high=100)

    category = factory.SubFactory(CategoryFactory)
    producer = factory.SubFactory(ProducerFactory)
    seller = factory.SubFactory(SellerFactory)

    class Meta:
        model = Product
        sqlalchemy_session = session


class ShopFactory(BaseFactory):
    name = FuzzyAttribute(lambda: f'Shop: {fake.company()}')
    address = factory.Faker('address')

    class Meta:
        model = Shop
        sqlalchemy_session = session


class OrderFactory(BaseFactory):
    status = FuzzyChoice(choices=OrderStatusEnum)
    datetime = factory.Faker('date_time_this_year')

    shop = factory.SubFactory(ShopFactory)

    class Meta:
        model = Order
        sqlalchemy_session = session


class OrderProductFactory(SQLAlchemyModelFactory):
    orders = factory.SubFactory(OrderFactory)
    products = factory.SubFactory(ProductFactory)
    amount = FuzzyInteger(low=10000, high=1000000)

    class Meta:
        model = OrderProduct
        sqlalchemy_session = session

