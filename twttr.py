def main():
    string = input("Write a string and I will remove all vowels from it: ")
    new_string = shorten(string)
    print(new_string)



def shorten(word):
    new_string = ""
    for char in word:
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() ==  "u":
            new_string += ""
        else:
            new_string += char
    return new_string


if __name__ == "__main__":
    main()