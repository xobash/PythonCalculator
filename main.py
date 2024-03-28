# Creating a simple Python-based calculator with tkinter.

# Importing tkinter library
import tkinter as tk

# Function to calculate the result.
def calculate():
    try:
        # Evaluating the expression from the entry widget
        result = eval(entry.get())
        # Displaying the result
        output_label.config(text="Result: " + str(result))
    except Exception as e:
        # Handling errors
        output_label.config(text="Error: Invalid Input")

# Creating the main window
root = tk.Tk()
root.title("Simple Python Calculator by xobash")
root.configure(bg="black")

# Creating entry widget
entry = tk.Entry(root, bg="black", fg="white", width=30)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Creating buttons and positioning them
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    # Creating buttons
    btn = tk.Button(root, text=text, width=5, height=2, bg="gray", fg="black", font=('Arial', '12', 'bold'))
    btn.grid(row=row, column=col)
    # Binding button click to entry widget
    btn.bind("<Button-1>", lambda event, text=text: entry.insert(tk.END, text))

# Creating equals button
equals_btn = tk.Button(root, text="=", width=5, height=2, bg="gray", fg="black", font=('Helvetica', '12', 'bold'))
equals_btn.grid(row=4, column=2)
equals_btn.bind("<Button-1>", lambda event: calculate())

# Creating label for output
output_label = tk.Label(root, bg="black", fg="white")
output_label.grid(row=5, column=0, columnspan=4)

# Running the main event loop
root.mainloop()
