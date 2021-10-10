#!/usr/bin/env python3
# example workign with conditionals
#By Eric October 2021

today = input("Is today a good day? y/n: ")
if today == "y":
    for x in range(10):
        print("Yes it is.")
elif today == "n":
    print("Really? I think it is lovely.")
else:
    print("I don't understand.")