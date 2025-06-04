# Arithmetic Operations Function

'''
define a function that performs basic arithmetic operations. 
This function, perform_operation, will be imported and used in a separate main.py script.
'''

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            results = num1 + num2
        case 'subtract':
            results = num1 - num2
        case 'multiply':
            results = num1 * num2
        case 'divide':
            if num2 == 0:
                results = f'Impossible to divide a number {num1} with {num2}'
            else:
                results = num1 / num2
    return results