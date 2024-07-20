import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to update the display
def update_display(symbol):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + symbol)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Create the display widget
display = tk.Entry(root, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Create buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the window
row_val = 1
col_val = 0
for button_text in button_texts:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18), command=evaluate_expression)
        button.bind('<Return>', evaluate_expression)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda text=button_text: update_display(text))
    button.grid(row=row_val, column=col_val, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 18), command=clear_display)
clear_button.grid(row=row_val, column=0, columnspan=4, sticky="nsew")

# Configure rows and columns for uniform button sizes
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()