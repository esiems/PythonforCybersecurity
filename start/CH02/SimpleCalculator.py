#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 

# Gather information from the user
first_number = int(input('What is the first number?'))
operation = input('+ * - /?')
second_number = int(input('What is the second number?'))

# Do the math. Think it through. There's a higher path for you.
if operation == '+':
    print(first_number + second_number)
if operation == '-':
    print(first_number - second_number)
if operation == '*':
    print(first_number * second_number)
if operation == '/':
    print(first_number / second_number)