# Temperature Conversion Tool

'''
Objective: 
Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and 
Fahrenheit, using global variables to store conversion factors.
'''

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

# Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit
def temperature_display():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
     
        if temp_type == 'F':
            conversion = convert_to_celsius(temperature)
            print(f"{temperature}°F is {conversion}°C")
        elif temp_type == 'C':
            conversion = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {conversion}°F")
        else:
            print('Invalid temperature Type')
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        
temperature_display()

