string = input("What did the deep thought say? ").strip().lower()

#string = string.strip()
#string = string.lower()

match string:
    case "42" | "forty two" | "forty-two":
        print("Yes")

    case _:
        print("No")