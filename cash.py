# TODO
from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars >= .01:
        break

cents = dollars * 100
#print(f"cents: {cents}")

quarters = int(cents//25)
cents = int(cents - (quarters * 25))
#print(f"quarters: {quarters}")
#print(f"cents: {cents}")

dimes = int(cents//10)
cents = int(cents - (dimes * 10))
#print(f"dimes: {dimes}")
#print(f"cents: {cents}")

nickels = int(cents//5)
cents = int(cents - (nickels * 5))
#print(f"nickels: {nickels}")
#print(f"cents: {cents}")

pennies = int(cents)
#print(f"pennies: {pennies}")

coins = int(quarters + dimes + nickels + pennies)
print(f"coins: {coins}")