from tkinter import Label, Entry, StringVar, OptionMenu, Button
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

    def output_sum(self, sum):
        print("Answer: " + str(sum))

    def output_diff(self, diff):
        print("Answer: " + str(diff))

    def output_product(self, product):
        print("Answer: " + str(product))

    def output_quotient(self, quotient):
        print("Answer: " + str(quotient))   

    def retry(self):
        again = input("Do you want to try again? (yes/no)")
        if again.lower() == "yes":
            return True
        elif again.lower() == "no":
            return False
        else: 
            print("Please enter yes or no only.")
#ask to try again