# cart_management-webpage

🛒 Shopping Cart Management System (Python OOP Console App)
📌 Description
This project is a console-based shopping cart management system implemented using Object-Oriented Programming (OOP) principles in Python. It simulates an online shopping experience where users can:

Browse through different product categories like Electronics, Clothing, and Food.

Add, remove, update, or clear items from a virtual shopping cart.

View cart items and place orders with 10% tax (GST) included.

The system uses OOP concepts like inheritance, encapsulation, and polymorphism, demonstrating clean architecture through classes like Item, Product, Electronics, Clothing, Food, and ShoppingCart.

🚀 Features
🛍 Add items to cart with quantity

🗑 Remove specific items from the cart

🔁 Update quantity of a product in the cart

🧾 View cart with total cost and GST

♻️ Clear all items from the cart

✅ Place order and show grand total

❌ Exit the system safely

🏗️ Object-Oriented Structure
Item (Base class) – Holds basic name and price

Product (Inherits Item) – Adds tax handling and cost calculation

Electronics / Clothing / Food (Inherits Product) – Add attributes like warranty, size, and expiry_date

ShoppingCart – Handles item operations: add, remove, update, view, clear, calculate total

📋 Sample Products
Electronics: Laptop, Headphones, Samsung S22 (with warranty)

Clothing: Shirt (Medium), Pant (Size 34)

Food: Apple, Banana, Papaya (with expiry dates)

💻 How to Run
Make sure you have Python installed (>=3.6)

Copy the code into a file named shopping_cart.py

Open a terminal and run:

bash
Copy
Edit
python shopping_cart.py
🧠 Concepts Used
Python OOP: Classes, Inheritance, super(), Method Overriding

Dictionaries and Lists

Input Validation and Error Handling

Console I/O and Menu Design

Basic Tax Calculation (10%)

📸 Sample Output
text
Copy
Edit
-----------------------> Start the shopping <---------------------
                     1. Add item to cart
                     2. Remove item from cart
                     3. View cart
                     4. Update item quantity
                     5. Clear cart
                     6. Place order
                     7. Exit

Enter your choice: 1

Available Products:
1. Laptop (Warranty: 12 months) - $40000.00
2. Headphones (Warranty: 6 months) - $3000.00
...
✅ Future Improvements
Add file-based cart saving

GUI version using Tkinter or PyQt

Login system and product search

Inventory stock management
