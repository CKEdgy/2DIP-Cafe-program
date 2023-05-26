import tkinter as tk
from tkinter import messagebox





class MenuApp(tk.Tk):
    def __init__(self, menu_items):
        super().__init__()
        self.title("Menu")
        self.menu_items = menu_items

        self.configure(bg='#ab0f41')
        self.geometry("400x400")
        self.spacing = 10

        self.menu_frame = tk.Frame(self, bg='#b6e7fc', padx=self.spacing, pady=self.spacing)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.menu_frame.configure(borderwidth=1, relief=tk.SOLID)  # Add border frame

        self.cart_frame = tk.Frame(self, bg='#b6e7fc', padx=self.spacing, pady=self.spacing)
        self.cart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.menu_label = tk.Label(self.menu_frame, text="Menu | Tahua", font=("Helvetica", 30, "bold"), bg='#b6e7fc', fg='#286393')
        self.menu_label.pack(pady=(0, self.spacing * 2))  # Increased separation

        for item, details in self.menu_items.items():
            item_frame = tk.Frame(self.menu_frame, bg='#b6e7fc')
            item_frame.pack(anchor='w')

            item_label = tk.Label(item_frame, text=f"{item}. {details['name']}: ${details['price']}",
                                  font=("Helvetica", 12, "italic", "bold"), bg='#b6e7fc',fg="#286393")
            item_label.grid(row=0, column=0, sticky='w', padx=(0, self.spacing * 2))  # Increased separation

            add_to_cart_button = tk.Button(item_frame, text=" + ", font=("Helvetica", 12),
                                           command=lambda i=details: self.add_to_cart(i))
            add_to_cart_button.grid(row=0, column=1, sticky='e')  # Align buttons to the right

        self.open_cart_button = tk.Button(self, text="🛒", font=("Helvetica", 15), command=self.open_cart)
        self.open_cart_button.pack(pady=(self.spacing * 2, self.spacing), padx=25)  # Increased separation and right padding

        self.cart_window = None
        self.cart_items = []

    def open_cart(self):
        if self.cart_window is None:
            self.cart_window = tk.Toplevel(self)
            self.cart_window.title("Shopping Cart")

            self.cart_label = tk.Label(self.cart_window, text="Shopping Cart", font=("Helvetica", 30, "bold"))
            self.cart_label.pack(pady=20)

            for item in self.cart_items:
                item_frame = tk.Frame(self.cart_window)
                item_frame.pack(anchor='w')

                item_label = tk.Label(item_frame, text=f"{item['name']}: ${item['price']}",
                                      font=("Helvetica", 12, "italic"), fg="brown")
                item_label.pack(side=tk.LEFT)

                remove_from_cart_button = tk.Button(item_frame, text="Remove", font=("Helvetica", 12),
                                                    command=lambda i=item: self.remove_from_cart(i))
                remove_from_cart_button.pack(side=tk.LEFT, padx=(10, 0))

            self.checkout_button = tk.Button(self.cart_window, text="Checkout", font=("Helvetica", 12, "bold"),
                                              command=self.checkout)
            self.checkout_button.pack(pady=(self.spacing * 2, 0))

            self.close_cart_button = tk.Button(self.cart_window, text="Close Cart", font=("Helvetica", 12, "bold"),
                                               command=self.close_cart)
            self.close_cart_button.pack(pady=10)



    def close_cart(self):
            if self.cart_window is not None:
                self.cart_window.destroy()
                self.cart_window = None
        

    

    def checkout(self):
        if self.cart_window is not None:
            checkout_window = tk.Toplevel(self.cart_window)
            checkout_window.title("Checkout")

            total_label = tk.Label(checkout_window, text="Total Price", font=("Helvetica", 30, "bold"))
            total_label.pack()

            total_price = sum(item['price'] for item in self.cart_items)
            total_price_label = tk.Label(checkout_window, text=f"${total_price:.2f}", font=("Helvetica", 30, "bold"))
            total_price_label.pack(pady=10)

            payment_label = tk.Label(checkout_window, text="Payment Method:", font=("Helvetica", 12, "bold"), fg="gray")
            payment_label.pack(pady=15)

            payment_var = tk.StringVar()

            click_collect_radio = tk.Radiobutton(checkout_window, text="Click and Collect", font=("Helvetica", 12),
                                                 variable=payment_var, value="Click and Collect")
            click_collect_radio.pack()

            eftpos_radio = tk.Radiobutton(checkout_window, text="Eftpos", font=("Helvetica", 12),
                                            variable=payment_var, value="Eftpos")
            eftpos_radio.pack()

            school_credit_radio = tk.Radiobutton(checkout_window, text="School Credit", font=("Helvetica", 12),
                                                   variable=payment_var, value="School Credit")
            school_credit_radio.pack()

            confirm_button = tk.Button(checkout_window, text="Confirm Purchase", font=("Helvetica", 12, "bold"),
                                       command=self.confirm_purchase)
            confirm_button.pack(pady=(self.spacing * 2, 0))

    def confirm_purchase(self):
        # Add your code here to handle the purchase confirmation
        print("Purchase confirmed!")


    def add_to_cart(self, item):
        self.cart_items.append(item)
        if self.cart_window is not None:
            item_frame = tk.Frame(self.cart_window, bg='white')
            item_frame.pack(anchor='w')

            item_label = tk.Label(item_frame, text=f"{item['name']}: ${item['price']}",
                                  font=("Helvetica", 12), bg='white')
            item_label.pack(side=tk.LEFT)

            remove_from_cart_button = tk.Button(item_frame, text="Remove", font=("Helvetica", 12),
                                                command=lambda i=item: self.remove_from_cart(i))
            remove_from_cart_button.pack(side=tk.LEFT, padx=(10, 0))

    def remove_from_cart(self, item):
        if self.cart_window is not None:
            for widget in self.cart_window.winfo_children():
                if isinstance(widget, tk.Frame):
                    item_label = widget.winfo_children()[0]
                    item_text = item_label.cget("text")
                    if item_text == f"{item['name']}: ${item['price']}":
                        widget.destroy()
                        self.cart_items.remove(item)
                        break


    def confirm_purchase(self):
        # Show a pop-up window to confirm the purchase
        messagebox.showinfo("Purchase Confirmation", "Purchase confirmed!")


        
if __name__ == '__main__':
    menu = {
        '1': {'name': 'Burger', 'price': 9.99},
        '2': {'name': '   Pizza', 'price': 8.99},
        '3': {'name': '  Salad', 'price': 5.99},
        '4': {'name': '   Soup', 'price': 4.99},
        '5': {'name': '   Fries', 'price': 3.99},
    }

    

    app = MenuApp(menu)
    app.mainloop()
