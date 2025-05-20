# Personal Finance Calculator
# Calculate the user’s monthly savings based on inputted monthly income and expenses

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
'''
Assume a simple annual interest rate of 5%.
Calculate the projected savings after one year, incorporating the interest. 
Use the simplified formula for annual savings projection: 
(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
'''
project_savings = (monthly_savings * 12) + (monthly_savings * 12 *0.05)

# Results
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {project_savings}")