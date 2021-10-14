#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By Eric
import platform
import os
from datetime import datetime

def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + message + "\n"
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "/pinger.log", "a")
    f.write(message)
    f.close()

def ping_address(ip_address):
    #Find OS
    current_os = platform.system().lower()

    #Find ping command based on OS
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        pinc_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    #run command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

for octet in range(254):
    # Assign IP to ping to a variable
    ip = "127.0.0.{0}".format(octet+1)
    exit_code = ping_address(ip)
    #print("{0}: {1}".format(ip,exit_code))
    write_log("{0}: {1}".format(ip, exit_code))