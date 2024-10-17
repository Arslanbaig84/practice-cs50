def main():
    vanity_plate = input("Enter a vanity plate: ")

    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")


def has_minimum_length(s):
    return len(s) >= 2


def has_maximum_length(s):
    return len(s) <= 6


def starts_with_letters(s):
    return s[:2].isalpha()


def check_numbers(s):
    numeric = ""
    found_digit = False
    for char in s:
        if found_digit:
            numeric += char
        elif char.isdigit():
            numeric += char
            found_digit = True

    if not s.isalpha():
        if numeric[0] == "0" or not numeric.isdigit():
            return False
        else:
            return True
    else:
        return True


def has_no_punctuation(s):
    return s.isalnum()


def is_valid(s):
    return (
        has_minimum_length(s)
        and has_maximum_length(s)
        and starts_with_letters(s)
        and check_numbers(s)
        and has_no_punctuation(s)
    )


if __name__ == "__main__":
    main()
