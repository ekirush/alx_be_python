'''
Objective: Implement a division calculator that robustly handles errors 
like division by zero and non-numeric inputs using command line arguments.

# Create 2 Python files:
    1. robust_division_calculator.py => which contains the division logic including error handling.
    2.  main.py => which interfaces with the user through the command line.
    
# Under robust_division_calculator.py
    1. Define a function safe_divide(numerator, denominator) that performs division, handling potential errors
        - Division by Zero: Use a try-except block to catch ZeroDivisionError.
        - Non-numeric Input: Attempt to convert arguments to floats. 
        Use a try-except block to catch ValueError for non-numeric inputs.
        - Return appropriate messages for errors or the result for successful division.
'''
        
def safe_divide(numerator, denominator):
    '''Performs division'''
    try:  
        division = float(numerator) / float(denominator)
        return f"The result of the division is {division}"
    except ZeroDivisionError as e:
        return (f"Error: Cannot divide by zero.")
    except ValueError as e:
        return (f"Error: Please enter numeric values only.")