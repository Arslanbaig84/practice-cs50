import sys
import csv
from tabulate import tabulate

menu = []

#handling file errors
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
#trying to open the file
    with open(sys.argv[1]) as file:
#reading data from file
        reader = csv.DictReader(file)
        for row in reader:
            if sys.argv[1] == "sicilian.csv":
                menu.append({"Sicilian Pizza" : row['Sicilian Pizza'], "Small" : row['Small'], "Large" : row['Large']})
            elif sys.argv[1] == "regular.csv":
                menu.append({"Regular Pizza" : row['Regular Pizza'], "Small" : row['Small'], "Large" : row['Large']})


#printing menu in tabulate form
        if sys.argv[1] == "sicilian.csv":
            print(tabulate(menu, headers = "keys", tablefmt = "grid"))
        elif sys.argv[1] == "regular.csv":
            print(tabulate(menu, headers = "keys", tablefmt = "grid"))

#handling file not found
except FileNotFoundError:
    sys.exit("File does not exist")
