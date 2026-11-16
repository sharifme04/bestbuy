class Product:
    """A specific product available in the store (e.g. MacBook Air M2)."""

    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the quantity in stock."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity. Deactivate the product if it reaches 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a string representing the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a given quantity; return the total price of the purchase."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if not self.active:
            raise ValueError(f"{self.name} is not available.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock of {self.name}: "
                             f"requested {quantity}, available {self.quantity}.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    """Try out the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
