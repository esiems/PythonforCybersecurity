#!/usr/bin/env python3
# example workign with Loops
#By Eric Siemssen, October 2021
x = input('How many times to you want to say "Hello World"')
for y in range(int(x)):
    print('Hello World')

students = ["David", "Eric", "Caleb", "Harry"]
for student in students:
    print("Hellow {0}".format(student))
    print(" How are you today.")