'''
Multiplication Table Generator
*******************************
Objective: Use a for loop to generate and print the multiplication table for a given number.
'''
number = int(input("Enter a number to see its multiplication table: "))

for num in range(1,11):
    product = num * number
    print(f"{number} * {num} = {product}")