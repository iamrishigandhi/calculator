import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            if any(c.isalpha() for c in current_text):
                raise ValueError("Invalid input")
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Division by zero")
        except ValueError as ve:
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"Error: {str(ve)}")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Invalid expression")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text.isdigit() or button_text in ('+', '-', '*', '/'):
        entry.insert(tk.END, button_text)
    elif button_text == '.':
        last_operand = current_text.split()[-1]
        if '.' not in last_operand:
            entry.insert(tk.END, button_text)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and output
entry = tk.Entry(root, font=("Helvetica", 32), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

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
    button = tk.Button(root, text=button_text, width=4, height=2, command=create_button_handler(button_text))
    button.grid(row=row_val, column=col_val, sticky="nsew")
    
    # Bind the <Configure> event to adjust font size dynamically
    button.bind("<Configure>", lambda event, button=button: adjust_button_font_size(event, button))
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure column and row weights
for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i + 1, weight=1)

# Function to adjust button font size based on button size
def adjust_button_font_size(event, button):
    new_font_size = max(10, int(event.width / 10))
    button['font'] = ('Helvetica', new_font_size)

# Add keyboard bindings
root.bind("<Return>", lambda event: on_click('='))
root.bind("<BackSpace>", lambda event: entry.delete(len(entry.get()) - 1))

# Run the main loop
root.mainloop()