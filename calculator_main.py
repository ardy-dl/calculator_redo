from calculator_ui import Calculator
from functions import Operation

calc = Calculator()
solve = Operation()

while True:
    num_1 = calc.input_num1()
    num_2 = calc.input_num2()

    sum = solve.addition(num_1, num_2)
    calc.output_sum(sum)
    quotient = solve.division(num_1, num_2)
    calc.output_quotient(quotient)

    if not calc.retry():
        break
