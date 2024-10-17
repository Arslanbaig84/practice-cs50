due = 50
cents = 0

while due > 0:
    print(f"Amount Due: {due}")
    cents = int(input("Insert Coin: "))

    while cents != 5 and cents != 10 and cents != 25:
        print(f"Amount Due: {due}")
        cents = int(input("Insert Coin: "))

    due = due - cents

print(f"Change Owed: {abs(due)}")
