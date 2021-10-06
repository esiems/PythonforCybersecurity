#!/usr/bin/env python3
# example workign with conditionals
#By Eric
# 
number = int(input("Choose a number between 1 and 4: ")) 
if number == 1:
    print("Wrong number, try again")
    print("I said try again, loser!")
elif number == 2:
    print("Wrong!")
elif number == 3:
    print("correct")
else:
    print("wrong")