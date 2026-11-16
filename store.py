from typing import List

import products
from products import Product


class Store:
    """A store that holds products (composition: a Store "has" Products)."""

    def __init__(self, product_list: List[Product]):
        self.products = list(product_list)

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Buy a list of (product, quantity) tuples; return the total price.

        The whole order is checked first, so nothing is bought if any
        item cannot be fulfilled.
        """
        requested = {}
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"{product.name} is not sold in this store.")
            if quantity <= 0:
                raise ValueError("Order quantity must be greater than 0.")
            requested[product] = requested.get(product, 0) + quantity

        for product, quantity in requested.items():
            if not product.is_active():
                raise Exception(f"{product.name} is not available.")
            if quantity > product.get_quantity():
                raise Exception(f"Not enough stock of {product.name}: "
                                f"requested {quantity}, "
                                f"available {product.get_quantity()}.")

        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(all_products[0], 1), (all_products[1], 2)]))


if __name__ == "__main__":
    main()
