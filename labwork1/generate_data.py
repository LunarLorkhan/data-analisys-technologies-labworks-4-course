import random
from itertools import cycle

import numpy as np
from sqlalchemy.orm.session import SessionTransaction

from engine import engine
from factories import *
from models import Base
from session import session


def generate_data(session: SessionTransaction):
    """Generate data using factories.

    Args:
        session: database transaction

    """
    categories = CategoryFactory.create_batch(size=30)
    producers = ProducerFactory.create_batch(size=15)

    products = []
    for _, category, producer in zip(range(10000), cycle(categories), cycle(producers)):
        products.append(
            ProductFactory(
                category=category,
                producer=producer,
            )
        )
    
    shops = ShopFactory.create_batch(size=15)
    
    orders = []
    order_statuses = list(OrderStatusEnum)
    for _, shop in zip(range(1000), cycle(shops)):
        status = random.choice(order_statuses).name
        orders.append(
            OrderFactory(
                shop=shop,
                status=status,
            )
        )
    
    for order in orders:
        for _ in range(random.randint(1, 15)):
            product = random.choice(products)
            products.remove(product)
            OrderProductFactory(
                orders=order,
                products=product,
            )


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # start transaction and generate data
    with session.begin() as session:
        generate_data(session)
