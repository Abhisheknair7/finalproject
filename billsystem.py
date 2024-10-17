import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        quantity = float(qty_text.get())
        price = float(price_text.get())
        total = quantity * price
        total_text.delete(0, tk.END)
        total_text.insert(0, f"{total:}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for Quantity and Price")

def add_to_table():
    global grand_total
    try:
        item = item_text.get()
        qty = float(qty_text.get())
        price = float(price_text.get())
        total = float(total_text.get())

        if not item:
            messagebox.showerror("Invalid Input", "Item name cannot be empty")
            return

        table.insert("", tk.END, values=(item, f"{qty:}", f"{price:}", f"{total:}"))

        item_text.delete(0, tk.END)
        qty_text.delete(0, tk.END)
        price_text.delete(0, tk.END)
        total_text.delete(0, tk.END)

        grand_total += total
        g_total.config(text=f"Grand Total: {grand_total:}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid inputs for Quantity, Price, and Total")




def reset():
    global grand_total
    table.delete(*table.get_children()) 
    grand_total = 0
    g_total.config(text=f"Grand Total: {grand_total:}")
    item_text.delete(0, tk.END)
    qty_text.delete(0, tk.END)
    price_text.delete(0, tk.END)
    total_text.delete(0, tk.END)



window = tk.Tk()
window.title("Billing System")
window.geometry("1000x650")
window.config(bg="white")



font_bold = ("Arial", 20, "bold")
font_normal = ("Arial", 16)


heading = tk.Label(window, text="BILLING SYSTEM", font=("Verdana", 35, "bold"), fg="red", bg="white")
heading.pack(pady=20)


item_details = tk.Frame(window)
item_details.pack(pady=20)


for col in range(4):
    item_details.columnconfigure(col, minsize=250)

item_label = tk.Label(item_details, text="Item Name", font=font_bold)
item_label.grid(row=0, column=0, padx=10, pady=5)

qty_label = tk.Label(item_details, text="Quantity", font=font_bold)
qty_label.grid(row=0, column=1, padx=10, pady=5)

price_label = tk.Label(item_details, text="Price", font=font_bold)
price_label.grid(row=0, column=2, padx=10, pady=5)

total_label = tk.Label(item_details, text="Total", font=font_bold)
total_label.grid(row=0, column=3, padx=10, pady=5)




item_text = tk.Entry(item_details, font=font_normal, width=15)
item_text.grid(row=1, column=0, padx=10, pady=5)

qty_text = tk.Entry(item_details, font=font_normal, width=15, justify="right")
qty_text.grid(row=1, column=1, padx=10, pady=5)

price_text = tk.Entry(item_details, font=font_normal, width=15, justify="right")
price_text.grid(row=1, column=2, padx=10, pady=5)

total_text = tk.Entry(item_details, font=font_normal, width=15, justify="right")
total_text.grid(row=1, column=3, padx=10, pady=5)




calc_btn = tk.Button(item_details, text='CALCULATE', font=font_normal, bg='blue', fg='white', command=calculate)
calc_btn.grid(row=2, column=2, padx=10, pady=10)

add_btn = tk.Button(item_details, text='ADD TO TABLE', font=font_normal, bg='blue', fg='white', command=add_to_table)
add_btn.grid(row=2, column=3, padx=10, pady=10)

reset_btn = tk.Button(item_details, text='RESET', font=font_normal, bg='red', fg='white', command=reset)
reset_btn.grid(row=2, column=0, padx=10, pady=10)


table = ttk.Treeview(item_details, columns=('item', 'qty', 'price', 'total'), show='headings', height=10)
table.grid(row=3, column=0, columnspan=4, pady=20, padx=10)

table.heading("#1", text='Item Name')
table.heading("#2", text='Quantity')
table.heading("#3", text='Price')
table.heading("#4", text='Total')


table.column("#1", width=300, anchor=tk.CENTER)
table.column("#2", width=200, anchor=tk.CENTER)
table.column("#3", width=200, anchor=tk.CENTER)
table.column("#4", width=300, anchor=tk.CENTER)


g_total = tk.Label(window, text="Grand Total: 0.00", fg='green', font=("Arial", 24, "bold"),)
g_total.pack(pady=10)


grand_total = 0


window.mainloop()

