from calculator_ui import Calculator
from functions import Operation

calc = Calculator()
solve = Operation()

calc.input_num1()
calc.input_num2()
sum = solve.addition(num_1, num_2)
print(sum)
