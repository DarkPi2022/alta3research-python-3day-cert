#!/usr/bin/env python3

"""This is a simple script to convert Celsius to Fahrenheit, and vice versa"""

def convert_temp(unit, source_temp):

    # this allows the input to be either F or f
    if (unit== "F") or (unit== "f"):

        # if the input unit is F or f, run this line
        return 'C', (source_temp - 32.0)*(5.0/9.0)

    # this allows the input to be either C or c
    elif (unit== "C") or (unit== "c"):

        # if the input is C or c, run this line
        return 'F', (source_temp * (9.0/5.0)) + 32.0

# prompts the user to input a unit
unit=input("Select (F) or (C): ")

# input from user
source_temp = float(input("What is the temperature: "))

# calculated value and temperature unit
u, t = convert_temp(unit, source_temp)

# prints the converted output with capitalized unit and rounded to one decimal point
print(source_temp, "degrees", unit.title(), "is", round(t, 1), "degrees", u)
