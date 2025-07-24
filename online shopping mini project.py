# Base Item class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

# Product class that handles tax and total cost calculations
class Product(Item):
    TAX_RATE = 0.1  # 10% tax rate

    def __init__(self, name, price):
        super().__init__(name, price)

    def total_cost(self, quantity):
        return quantity * self.price * (1 + Product.TAX_RATE)

# Electronics class extending Item with warranty attribute
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty  # Warranty in months

    def __str__(self):
        return f"{self.name} (Warranty: {self.warranty} months) - ${self.price:.2f}"

# Clothing class extending Item with size attribute
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{self.name} (Size: {self.size}) - ${self.price:.2f}"

# Food class extending Item with expiry date attribute
class Food(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name} (Expires on: {self.expiry_date}) - ${self.price:.2f}"

# Shopping cart class to manage items
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}
        print(f"{quantity} x {product.name} added to the cart.")

    def remove_item(self, product_name):
        if product_name in self.items:
            del self.items[product_name]
            print(f"{product_name} removed from the cart.")
        else:
            print(f"{product_name} not found in the cart.")

    def update_item(self, product_name, quantity):
        if product_name in self.items:
            self.items[product_name]['quantity'] = quantity
            print(f"{product_name} updated to {quantity} in the cart.")
        else:
            print(f"{product_name} not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nCart contents:")
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{quantity} x {product} (Total: ${product.total_cost(quantity):.2f})")

    def clear_cart(self):
        self.items.clear()
        print("Cart cleared.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].total_cost(item['quantity'])
        return total

# Function to display the shopping menu
def show_menu():
    print("\n-----------------------> Start the shopping <---------------------")
    print(20 * " ", "1. Add item to cart")
    print(20 * " ", "2. Remove item from cart")
    print(20 * " ", "3. View cart")
    print(20 * " ", "4. Update item quantity")
    print(20 * " ", "5. Clear cart")
    print(20 * " ", "6. Place order")
    print(20 * " ", "7. Exit")

# Function to display available products
def display_products(products):
    print("\nAvailable Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product}")

# Main process function
def main():
    # Creating product instances
    products = [
        Electronics("Laptop", 40000, 12),
        Electronics("Headphones", 3000, 6),
        Electronics("SamsungS22", 82000, 18),
        Clothing("Shirt", 600, "Medium"),
        Clothing("Pant", 1200, "34"),
        Food("Apple", 50, "2024-04-30"),
        Food("Banana", 10, "2024-04-30"),
        Food("Papaya", 60, "2024-04-30")
    ]

    # Initializing shopping cart
    cart = ShoppingCart()

    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                display_products(products)
                product_idx = int(input("Enter the product number to add to cart: ")) - 1
                quantity = int(input("Enter quantity: "))
                if 0 <= product_idx < len(products):
                    product = products[product_idx]
                    cart.add_item(product, quantity)
                else:
                    print("Invalid product selection.")

            elif choice == 2:
                cart.view_cart()
                product_name = input("Enter the product name to remove: ")
                cart.remove_item(product_name)

            elif choice == 3:
                cart.view_cart()

            elif choice == 4:
                cart.view_cart()
                product_name = input("Enter the product name to update: ")
                quantity = int(input("Enter new quantity: "))
                cart.update_item(product_name, quantity)

            elif choice == 5:
                cart.clear_cart()

            elif choice == 6:
                cart.view_cart()
                if input("Do you want to place the order? (yes/no): ").lower() == "yes":
                    total = cart.calculate_total()
                    print(f"\nTotal amount (with 10% GST): ${total:.2f}")
                    print("Order placed successfully!")
                    cart.clear_cart()
                else:
                    print("Order not placed.")

            elif choice == 7:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid option. Please choose again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
