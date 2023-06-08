from calculator_ui import Calculator
from functions import Operation

calc = Calculator()
solve = Operation()

num_1 = calc.input_num1()
num_2 = calc.input_num2()

sum = solve.addition(num_1, num_2)
calc.output_sum(sum)
