#!/usr/bin/env python3
# Second example of pinging from Python
# By 
# import necessary Python modules
import platform
import os


for octet in range(254):
    # Assign IP to ping to a variable
    ip = "127.0.0.{0}".format(octet+1)

    #Find OS
    current_os = platform.system().lower()

    #Find ping command based on OS
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        pinc_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    #run command and capture exit code
    exit_code = os.system(ping_cmd)
    print("{0}: {1}".format(ip,exit_code))