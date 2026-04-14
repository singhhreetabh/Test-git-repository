import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Set theme
        self.root.configure(bg='#2c3e50')

        # Expression and result
        self.expression = ""
        self.history = []

        # Entry field
        self.entry = tk.Entry(root, font=('Arial', 24), bg='#ecf0f1', fg='#2c3e50', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('sqrt', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('History', 7, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=('Arial', 18), bg='#3498db', fg='white',
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Configure grid weights
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == 'History':
            self.show_history()
        elif char in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            self.expression += char + '('
            self.update_entry()
        elif char == 'pi':
            self.expression += str(math.pi)
            self.update_entry()
        elif char == 'e':
            self.expression += str(math.e)
            self.update_entry()
        else:
            self.expression += str(char)
            self.update_entry()

    def calculate(self):
        try:
            # Replace ^ with **
            expr = self.expression.replace('^', '**')
            # Evaluate
            result = eval(expr)
            self.history.append(f"{self.expression} = {result}")
            self.expression = str(result)
            self.update_entry()
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")
            self.clear()

    def clear(self):
        self.expression = ""
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No calculations yet.")
        else:
            hist_text = "\n".join(self.history[-10:])  # Last 10
            messagebox.showinfo("History", hist_text)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()