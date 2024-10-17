import sys
grocery = {}

counter = 1

while True:
    try:
        key = input("")
        if key not in grocery:
            grocery[key] = (counter)
        else:
            grocery[key] += 1
    except EOFError:
        print("\n")
        sorted_keys = sorted(grocery.keys(), key=lambda x: x.upper())
        for key in sorted_keys:
            print(grocery[key], key.upper())
        sys.exit(0)