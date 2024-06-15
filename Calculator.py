
from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg="lightgrey")  # Set background color for the main window

        # Define variables
        self.value = StringVar()
        self.v1 = None
        self.op = None
        self.memory = 0

        # Textfield for displaying input and output
        self.result_field = Entry(master, textvariable=self.value, font=("Arial", 16), bg="white")
        self.result_field.grid(row=0, columnspan=5, padx=10, pady=10)

        # Button creation with a function call on click
        button_list = [
            "7", "8", "9", "/", "sqrt",
            "4", "5", "6", "*", "exp",
            "1", "2", "3", "-", "M+",
            "0", ".", "%", "+", "M-"
        ]
        row = 1
        col = 0
        for button_text in button_list:
            button = Button(master, text=button_text, command=lambda txt=button_text: self.button_click(txt),
                            font=("Arial", 12), width=5, height=2, bg="lightblue")
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        
        self.clear_button = Button(master, text="C", command=self.clear_all, font=("Arial", 12), width=5, height=2, bg="lightcoral")
        self.clear_button.grid(row=5, column=0, padx=5, pady=5)

        self.equals_button = Button(master, text="=", command=self.calculate, font=("Arial", 12), width=11, height=2, bg="lightgreen")
        self.equals_button.grid(row=5, columnspan=4, padx=5, pady=5, column=1)

    def button_click(self, button_text):
        try:
            if button_text.isdigit() or button_text == ".":
                self.value.set(self.value.get() + button_text)
            elif button_text in {"+", "-", "*", "/", "%"}:
                self.v1 = float(self.value.get())
                self.op = button_text
                self.value.set("")
            elif button_text == "sqrt":
                self.v1 = float(self.value.get())
                result = math.sqrt(self.v1)
                self.value.set(str(result))
            elif button_text == "exp":
                self.v1 = float(self.value.get())
                result = math.exp(self.v1)
                self.value.set(str(result))
            elif button_text == "M+":
                self.memory += float(self.value.get())
                self.value.set("")
            elif button_text == "M-":
                self.memory -= float(self.value.get())
                self.value.set("")
        except ValueError:
            self.value.set("Error: Invalid input")

    def clear_all(self):
        self.value.set("")
        self.v1 = None
        self.op = None

    def calculate(self):
        try:
            v2 = float(self.value.get())
            result = None
            if self.op == "+":
                result = self.v1 + v2
            elif self.op == "-":
                result = self.v1 - v2
            elif self.op == "*":
                result = self.v1 * v2
            elif self.op == "/":
                if v2 == 0:
                    self.value.set("Error: Division by zero")
                    return
                else:
                    result = self.v1 / v2
            elif self.op == "%":
                result = self.v1 % v2
            self.value.set(str(result))
        except ValueError:
            self.value.set("Error: Invalid input")
        except TypeError:
            self.value.set("Error: Incomplete operation")

# Create the main window and run the application
root = Tk()
calculator = Calculator(root)
root.mainloop()
