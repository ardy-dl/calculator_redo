from calculator_ui import Calculator
from functions import Operation

calc = Calculator()
solve = Operation()

while True:
    try:
        operation = input("Select an operation: (+, -, *, /): ")
        num_1 = calc.input_num1()
        num_2 = calc.input_num2()

        if operation == "+":
            sum = solve.addition(num_1, num_2)
            calc.output_sum(sum)        
        elif operation == "-":
            diff = solve.subtraction(num_1, num_2)
            calc.output_diff(diff)
        elif operation == "*":
            product = solve.multiplication(num_1, num_2)
            calc.output_product(product)
        elif operation == "/":
            quotient = solve.division(num_1, num_2)
            calc.output_quotient(quotient)
        else: 
            print("Invalid operation")

    except ValueError:
        print("Error:", "Sorry! Only numbers are accepted.")

    if not calc.retry():
        break
