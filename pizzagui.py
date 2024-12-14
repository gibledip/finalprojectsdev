# SalazarlorenzoFinalProject.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PizzaOrderingApp:
    """A GUI application for ordering pizza, including options for size, toppings, and quantity."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Ordering System")
        self.root.geometry("400x400")
        
        # Stores orders
        self.orders = []
        
        # Main Window
        self.main_window()

    def main_window(self):
        """Displays the main window."""
        self.clear_window()
        
        tk.Label(self.root, text="Welcome to Pizza Ordering System", font=("Arial", 16)).pack(pady=10)
        img = Image.open("pizza.png").resize((100, 100))
        pizza_image = ImageTk.PhotoImage(img)
        self.pizza_img_label = tk.Label(self.root, image=pizza_image, text="Pizza Image", compound="bottom")
        self.pizza_img_label.image = pizza_image  # Prevent garbage collection
        self.pizza_img_label.pack()

        tk.Button(self.root, text="Order Pizza", command=self.order_window, font=("Arial", 14)).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14)).pack(pady=5)

    def order_window(self):
        """Displays the order window."""
        self.clear_window()
        
        tk.Label(self.root, text="Order Your Pizza", font=("Arial", 16)).pack(pady=10)
        
        # Pizza Size
        tk.Label(self.root, text="Pizza Size:", font=("Arial", 12)).pack()
        self.size_var = tk.StringVar(value="Medium")
        for size in ["Small", "Medium", "Large"]:
            tk.Radiobutton(self.root, text=size, variable=self.size_var, value=size).pack()
        
        # Toppings
        tk.Label(self.root, text="Toppings:", font=("Arial", 12)).pack()
        self.toppings_var = tk.StringVar(value="Cheese")
        for topping in ["Cheese", "Pepperoni", "Vegetables"]:
            tk.Radiobutton(self.root, text=topping, variable=self.toppings_var, value=topping).pack()
        
        # Quantity
        tk.Label(self.root, text="Quantity:", font=("Arial", 12)).pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)
        
        # Buttons
        tk.Button(self.root, text="Add to Order", command=self.add_to_order).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_window).pack(pady=5)

    def add_to_order(self):
        """Validates input and adds the order."""
        try:
            quantity = int(self.quantity_entry.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a positive integer.")
            return
        
        size = self.size_var.get()
        topping = self.toppings_var.get()
        price = self.calculate_price(size, topping, quantity)
        self.orders.append({"size": size, "topping": topping, "quantity": quantity, "price": price})
        messagebox.showinfo("Order Added", f"Added: {quantity}x {size} Pizza with {topping} - ${price:.2f}")
        self.main_window()

    def calculate_price(self, size, topping, quantity):
        """Calculates the price based on size, topping, and quantity."""
        size_prices = {"Small": 8, "Medium": 10, "Large": 12}
        topping_prices = {"Cheese": 1, "Pepperoni": 2, "Vegetables": 1.5}
        return (size_prices[size] + topping_prices[topping]) * quantity

    def clear_window(self):
        """Clears the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderingApp(root)
    root.mainloop()
