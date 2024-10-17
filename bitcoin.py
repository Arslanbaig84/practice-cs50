# Demonstrates json

import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
)
o = response.json()
#print(o)

price = o["bpi"]["USD"]["rate"]

price = price.replace(",", "")

total = float(price) * float(sys.argv[1])
print(f"${total:,.4f}")