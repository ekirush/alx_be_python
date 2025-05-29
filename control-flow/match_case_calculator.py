'''
Simple Calculator with Match Case
**********************************
Objective: 
Learn to use Match Case statements for handling multiple operations in a simple calculator program.
'''

num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):") # Enter operation of the choice

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Enter correct input")
        
print(f"The result is {result}")