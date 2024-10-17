import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.strip().split(".")
    valid = True
    for part in parts:
        if not re.search(r"^(?!0\d)\d{1,3}$", part) or int(part) < 0 or int(part) > 255 or len(parts) != 4:
            valid = False
            break
    return valid

if __name__ == "__main__":
    main()