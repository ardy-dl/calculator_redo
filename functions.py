# create operations class

class Operation:
    #create operations
    def addition(self, num_1, num_2):
        result = num_1 + num_2
        return result
    
    def subtraction(self, num_1, num_2):
        result = num_1 - num_2
        return result
    
    def multiplication(self, num_1, num_2):
        result = num_1 * num_2
        return result
    
    def division(self, num_1, num_2):
        if num_2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num_1 / num_2
            return result
        

    

        


    

        