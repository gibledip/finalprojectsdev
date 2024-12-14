import tkinter as tk
from tkinter import messagebox


class PizzaOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Ordering System")
        self.root.geometry("400x400")
        
        # Order storage
        self.orders = []
        
        # Navigate to Main Window
        self.main_window()

    def main_window(self):
        """Creates the main window of the application."""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main Window Layout
        title_label = tk.Label(self.root, text="Welcome to Pizza Ordering System", font=("Arial", 16))
        title_label.pack(pady=20)

        order_button = tk.Button(self.root, text="Order Pizza", command=self.order_window, font=("Arial", 14))
        order_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14))
        exit_button.pack(pady=10)

    def order_window(self):
        """Creates the order window where users can input their pizza preferences."""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Order Window Layout
        tk.Label(self.root, text="Select Your Pizza", font=("Arial", 16)).pack(pady=10)

        # Pizza Size
        tk.Label(self.root, text="Pizza Size:", font=("Arial", 12)).pack()
        self.size_var = tk.StringVar(value="Medium")
        sizes = ["Small", "Medium", "Large"]
        for size in sizes:
            tk.Radiobutton(self.root, text=size, variable=self.size_var, value=size).pack()

        # Toppings
        tk.Label(self.root, text="Toppings:", font=("Arial", 12)).pack()
        self.toppings_var = tk.StringVar(value="Cheese")
        toppings = ["Cheese", "Pepperoni", "Vegetables"]
        for topping in toppings:
            tk.Radiobutton(self.root, text=topping, variable=self.toppings_var, value=topping).pack()

        # Quantity
        tk.Label(self.root, text="Quantity:", font=("Arial", 12)).pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)

        # Buttons
        tk.Button(self.root, text="Add to Order", command=self.add_to_order).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_window).pack(pady=5)

    def add_to_order(self):
        """Validates input, adds the order, and displays an order summary."""
        # Validate Input
        try:
            quantity = int(self.quantity_entry.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid quantity.")
            return

        size = self.size_var.get()
        topping = self.toppings_var.get()

        # Add order to the list
        order = {
            "size": size,
            "topping": topping,
            "quantity": quantity,
            "price": self.calculate_price(size, topping, quantity)
        }
        self.orders.append(order)

        # Confirmation Message
        messagebox.showinfo("Order Added", f"Order Summary:\nSize: {size}\nTopping: {topping}\nQuantity: {quantity}\nTotal: ${order['price']:.2f}")

        # Navigate to Order Summary Window
        self.order_summary_window()

    def calculate_price(self, size, topping, quantity):
        """Calculates the price of the order."""
        # Prices for sizes and toppings
        size_prices = {"Small": 8, "Medium": 10, "Large": 12}
        topping_prices = {"Cheese": 1, "Pepperoni": 2, "Vegetables": 1.5}

        base_price = size_prices[size]
        topping_price = topping_prices[topping]
        return (base_price + topping_price) * quantity

    def order_summary_window(self):
        """Displays the order summary and provides options to confirm or cancel."""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Order Summary Layout
        tk.Label(self.root, text="Order Summary", font=("Arial", 16)).pack(pady=10)

        if not self.orders:
            tk.Label(self.root, text="No orders placed yet.", font=("Arial", 12)).pack(pady=10)
        else:
            for order in self.orders:
                tk.Label(self.root, text=f"{order['quantity']}x {order['size']} Pizza with {order['topping']} - ${order['price']:.2f}",
                         font=("Arial", 12)).pack(pady=5)

        # Buttons
        tk.Button(self.root, text="Confirm Order", command=self.confirm_order).pack(pady=10)
        tk.Button(self.root, text="Cancel Order", command=self.main_window).pack(pady=5)

    def confirm_order(self):
        """Confirms the order and displays the total price."""
        if self.orders:
            total_price = sum(order['price'] for order in self.orders)
            messagebox.showinfo("Order Confirmed", f"Your total is ${total_price:.2f}. Thank you for ordering!")
            self.orders = []  # Clear orders after confirmation
            self.main_window()
        else:
            messagebox.showerror("No Orders", "No orders to confirm.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderingApp(root)
    root.mainloop()