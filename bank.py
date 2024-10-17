def main():
    greet = input("Greeting: ").strip()

    owed = value(greet)
    print(f"${owed}")


def value(greet):
    greet = greet.lower()
    first = greet.split()[0]

    if greet == "hello" or first == "hello,":
        return 0
    elif first[0] == "h":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()