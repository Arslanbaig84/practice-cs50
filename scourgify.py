import sys
import csv

#handling file errors
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
#trying to open the file
    with open(sys.argv[1],'r') as file:

#reading data from file
        reader = csv.DictReader(file)

        file_data = []
        for index, row in enumerate(reader):
            full_name = row['name']
            house = row['house']
            last, first = full_name.split(",")
            first = first.strip(" ")

            file_data.append({"first" : first, "last" : last, "house" : house})

#    sorted_data = sorted(file_data, key=lambda x: x['first'])

#handling file not found
except FileNotFoundError:
    sys.exit(f"Could not read csv '{sys.argv[1]}'")

try:
#opening file for writing
    with open(sys.argv[2], "w") as file:

        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader() #include header in file
        writer.writerows(file_data)
#       writer.writerows({"first" : file_data['first'], "last" : file_data['last'].strip(" "), "house" : file_data['house']})

except FileNotFoundError:
    sys.exit(f"Could not open csv '{sys.argv[2]}'")
