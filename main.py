import products
import store


def list_products(store_obj):
    """Print all active products in the store, numbered."""
    print("------")
    for i, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{i}. ", end="")
        product.show()
    print("------")


def show_total_quantity(store_obj):
    """Print the total number of items in the store."""
    print(f"Total of {store_obj.get_total_quantity()} items in store")


def make_order(store_obj):
    """Let the user pick products and quantities, then place the order."""
    available = store_obj.get_all_products()
    list_products(store_obj)
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product_choice = input("Which product # do you want? ").strip()
        if product_choice == "":
            break
        if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(available):
            print("Invalid product number.")
            continue

        amount = input("What amount do you want? ").strip()
        if not amount.isdigit() or int(amount) <= 0:
            print("Invalid amount.")
            continue

        shopping_list.append((available[int(product_choice) - 1], int(amount)))
        print("Product added to list!")

    if not shopping_list:
        return

    try:
        total_price = store_obj.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as error:
        print(f"Error while making order! {error}")


def start(store_obj):
    """Show the store menu and handle the user's choices."""
    actions = {
        "1": list_products,
        "2": show_total_quantity,
        "3": make_order,
    }

    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()
        if choice == "4":
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice, please enter a number from 1 to 4.")
        else:
            action(store_obj)


def main():
    """Set up the default inventory and start the store menu."""
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
