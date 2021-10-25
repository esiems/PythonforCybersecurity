#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Eric Siemssen 
source_message = input("What is the message")
source_message = source_message.lower()
final_message = ""
for letter in source_message:
    ascii_num = ord(letter)
    if ascii_num>=97 and ascii_num<=122:
        new_ascii = ascii_num + 13
        if new_ascii > 122:
            new_ascii = new_ascii -26
        final_message = final_message + str(new_ascii)
    else:
        final_message = final_message + str(ascii_num)
print("converted")
print(final_message)
