#!/usr/bin/env python3
# First example of pinging from Python
# By Eric Siemssen

# import the python modules
import os
import platform

#Assign Ip Address
ip = "127.0.0.1"

#Created the ping command
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

#Run command
exit_code = os.system(ping_cmd)
print(exit_code)