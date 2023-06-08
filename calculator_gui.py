from tkinter import Label, Entry, StringVar, OptionMenu, Button
from tkinter import messagebox
#ask user for operation
#ask user for input 1 and 2
class Calculator:
    def __init__(self, root, calc):
        self.root = root
        self.root.title = "Calculator"
        self.calc = calc
        self.create_widgets()

    def create_widgets(self):
        #input fields title
        num_1_label = Label(self.root, text = "Enter the first number: ")
        num_1_label.pack()

        self.num_1_entry = Entry(self.root)
        self.num_1_entry.pack()

        num_2_label = Label(self.root, text = "Enter the second number: ")
        num_2_label.pack()

        self.num_2_entry = Entry(self.root)
        self.num_2_entry.pack()

        self.operation_var = StringVar()
        self.operation_var.set("+")

        self.operation_options = ["+", "-", "*", "/"]
        self.operation_dropdown = OptionMenu(self.root, self.operation_var, *self.operation_options)
        self.operation_dropdown.pack()

        self.calculate_button = Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        num_1 = float(self.num_1_entry.get())
        num_2 = float(self.num_2_entry.get())
        operation = self.operation_var.get()

        if operation == "+":
            result = self.calc.addition(num_1, num_2)
            self.output_sum(result)
        elif operation == "-":
            result = self.calc.subtraction(num_1, num_2)
            self.output_diff(result)
        elif operation == "*":
            result = self.calc.multiplication(num_1, num_2)
            self.output_product(result)
        elif operation == "/":
            result = self.calc.division(num_1, num_2)
            self.output_quotient(result)
        else:
            print("Invalid operation")

        self.output_result(result)

    def output_sum(self, sum):
        print("Answer: " + str(sum))
    
    def output_diff(self, diff):
        print("Answer: " + str(diff))

    



    def output_result(self, result):
        messagebox.showinfo("Result", "The answer is: " + str(result))
