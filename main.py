import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and output
entry = tk.Entry(root, width=20, font=("Helvetica", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Added sticky attribute

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Function to generate button click event handlers
def create_button_handler(button_text):
    return lambda: on_click(button_text)

# Add buttons to the grid
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=5, height=2, command=create_button_handler(button_text))
    button.grid(row=row_val, column=col_val, sticky="nsew")  # Added sticky attribute
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure column and row weights
for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i + 1, weight=1)

# Run the main loop
root.mainloop()