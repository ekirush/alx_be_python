# Explore `datetime` Module

'''
Objective: 
Familiarize yourself with Python’s datetime module by writing a script that performs 
specified operations with dates and times.
'''
from datetime import date, time, datetime, timedelta

def display_current_datetime ():
    '''Function that displays current date and time'''
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
    return current_date
 
# Prompt user to enter the number of days to add to the current date
num_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    '''
    Function that calculate future date by combining current datetime and 
    user input of number of days to be added to the current date.
    '''
    future_date = display_current_datetime() + timedelta(days=num_of_days)
    print(f"Future date: {future_date}")
    return future_date

# Print the  results 
calculate_future_date()
    