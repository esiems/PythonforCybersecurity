#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 
import os
import crypt
def read_dictionary(dictionary_file):
    script_path=os.path.realpath(__file__)
    script_folder=os.path.split(script_path)
    f = open(script_folder[0] + "/" + dictionary_file, "r")
    file_contents=f.read()
    return file_contents

def evaluate_password(hashed_password, algorithm_salt, \
     plaintext_password):
    crypted_password = crypt.crypt(plaintext_password,\
        algorithm_salt)
    if crypted_password == hashed_password:
        return True
    return False
password_file = input("What is the password file? ")
hashed_password = input("What is the hashed password? ")
algorithm_salt = input("What is the algorithm salf? ")

passwords = read_dictionary(password_file)


for password in passwords.splitlines():
    result = evaluate_password(hashed_password,\
         algorithm_salt, password)
    if result:
        print("Match found: {0}".format(password))
        break