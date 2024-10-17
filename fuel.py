import sys

def main():
    fuel = input("Fuel(n/d): ")
    fuel = convert(fuel)
    fuel = gauge(fuel)

    print(fuel)


def convert(fuel):
    if "/" not in fuel:
        raise ValueError
    n, d = fuel.split("/")
    try:
        n = int(n)
        d = int(d)
    except ValueError:
        raise ValueError
    if d == 0:
        raise ZeroDivisionError
    if n > d:
        raise ValueError

    z = float(n)/float(d)
    #print(z)
    z = z * 100
    #print(z)
    return round(z)

def gauge(z):
    #print(z)
    if z <= 1:
        return "E"
    elif z >= 99:
        return "F"
    else:
        return (f"{z}%")


if __name__ == "__main__":
    main()