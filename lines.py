import sys


rows = []
try:
#trying to open the file
    with open(sys.argv[1]) as file:
#handling file errors
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
#reading data from file
        for line in file:
            row = line.strip()
            rows.append(row)

#counter to count number of rows
    count = 0
    for row in rows:
        if not row.startswith("#") and row.strip() != "":
            count += 1
        else:
            count = count
    print(count)
#handling file not found
except FileNotFoundError:
    sys.exit("File does not exist")
