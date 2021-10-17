#!/usr/bin/env python3
# example workign with Functions
#By Eric
def send_message(loops):
    for x in range(loops):
        print("Yes it is.")

today = input("Is today a good day? y/n: ")
if today == "y":
    send_message(10)
elif today == "n":
    print("Really? I think it is lovely.")
else:
    print("I don't understand.")