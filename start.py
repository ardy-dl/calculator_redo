# Tkinter start-up
from tkinter import Tk
# import other files
from calculator_gui import Calculator
from functions import Operation

# rooting
def main():
    root = Tk()
    root.title("Calculator")
    root.geometry("300x160")
    calc = Operation()
    gui = Calculator(root, calc)
    root.mainloop()

# Making sure that file only runs from here
if __name__ == "__main__":
    main()


