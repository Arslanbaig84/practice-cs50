import re

# Type um, followed by Enter. Your count function should return 1.
# Type um?, followed by Enter. Your count function should return 1.
# Type Um, thanks for the album., followed by Enter. Your count function should return 1.
# Type Um, thanks, um..., followed by Enter. Your count function should return 2.

def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    words = s.split(" ")
    for word in words:
        if matches := re.search(r"\bum\b", word, re.IGNORECASE):
            counter += 1
    return counter


if __name__ == "__main__":
    main()