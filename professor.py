import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x1 = generate_integer(level)
        y1 = generate_integer(level)
        addition = x1 + y1
        for j in range(3):
            try:
                answer = int(input(f"{x1} + {y1} = "))
                if answer ==  addition:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                continue
        print(addition)
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level(1 - 3): "))
            if level > 0 and level <= 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return(random.randint(0, 9))
    elif level == 2:
        return(random.randint(10, 99))
    else:
        return(random.randint(100, 999))


if __name__ == "__main__":
    main()

#x1 = random.randint(1,10)