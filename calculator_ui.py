#ask user for operation
#ask user for input 1 and 2
class Calculator:
    def input_num1(self):
        num_1 = float(input("Enter a number: "))
        return num_1
    
    def input_num2(self):
        num_2 = float(input("Enter a number: "))
        return num_2
    
    def output_sum(self, sum):
        print("Answer: " + str(sum))
#ask to try again