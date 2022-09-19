import random
from collections import defaultdict
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
    products = ProductFactory.create_batch(20000)

    # generate for product 1 - 4 category
    for product in products:
        caterories_for_product = random.choices(categories, k=random.randint(1, 4))
        for category_for_product in caterories_for_product:
            CategoryProductAssociation(
                products=product,
                categories=category_for_product,
            )

    warehouse_product_dict = defaultdict(list)
    warehouses = WarehouseFactory.create_batch(5)
    # link warehouses and products
    for warehouse in warehouses:
        splitted_products = np.array_split(products, 5)
        for products_sample in splitted_products:
            for product in products_sample:
                ProductWarehouseAssociation(
                    products=product,
                    warehouses=warehouse,
                )
                warehouse_product_dict[warehouse].append(product)

    shops = ShopFactory.create_batch(15)

    # get one warehouse for each shop
    # Example:
    # >>> warehouse = ['one', 'two', 'three']
    # >>> shops = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # >>> shop_warehouses = zip(cycle(warehouses), shops)
    # >>> shop_warehouses
    # [
    #   ('one', 1), ('two', 2), ('three', 3),
    #   ('one', 4), ('two', 5), ('three', 6),
    #   ('one', 7), ('two', 8), ('three', 9)
    # ]
    shop_warehouses = zip(cycle(warehouses), shops)
    # generate 300 orders per shop
    for warehouse, shop in shop_warehouses:
        orders = OrderFactory.create_batch(
            300,
            shop=shop,
            warehouse=warehouse,
        )

        # fill products for each order
        for order in orders:
            products = warehouse_product_dict[warehouse]
            for product in random.choices(products, k=random.randint(1, len(products))):
                OrderProductAssociation(
                    products=product,
                    orders=order,
                    amount=random.randint(1000, 10000),
                )


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # start transaction and generate data
    with session.begin() as session:
        generate_data(session)
