'''
Personal Daily Reminder
************************
Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops 
to remind the user about a single, priority task for the day based on time sensitivity.
******************************************************************************************************
Task Description:

Develop a script named daily_reminder.py. 
This script will ask the user for a single task, its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder for that task, 
demonstrating control flow and loops without relying on data structures to store multiple tasks.
'''

task = input('Enter your task: ')
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        message = f"Reminder: {task} is a high priority task "
    case 'medium':
        message = f"{task} is a medium priority task "
    case 'low':
        message = f"Note: {task} is a low priority task "
    case _:
        message = 'Enter Correct Priority'
        
if time_bound == 'yes':
    message += "task that requires immediate attention today!"
elif time_bound == 'no':
    message += "consider completing it when you have free time."
else:
    message = ("Enter correct time bound")


print(message)