#!/usr/bin/env python3
# Sample script that writes to a file
# By Eric 10/13
import os
script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)
hackme = open(script_folder[0] + "/hackme.txt", "w")

def ask(q, s, file):
    
    a = input(q + " ")
    file.write("\n" + s + " " + a)

ask("What is your name?", "My name is", hackme)
ask("What is your favorite color", "My favorite color is", hackme)
ask("What was your first pet's name?", "My first pet's name is", hackme)
ask("What is your mothers' maiden name?", "My mothers' maiden name is", hackme)
ask("What elementary school did you attend", "My elementary school was", hackme)
hackme.close()