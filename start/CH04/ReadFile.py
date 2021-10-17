#!/usr/bin/env python3
# Sample script that reads from a file
# By Eric, 10/17
import os
script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)
hackme = open(script_folder[0] + "/hackme.txt", "r")
print("Here's some info to hack me with:")
print(str(hackme.read()))