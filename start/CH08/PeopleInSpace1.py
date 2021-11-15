import requests
import json

url = "https://icanhazdadjoke.com"

payload={}
headers = {"Accept":"application/json"}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

dadjokes = response.json()
print(dadjokes["joke"])