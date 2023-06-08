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