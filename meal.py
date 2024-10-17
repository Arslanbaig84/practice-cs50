def main():
    meal_time = input("Time: ")
    time = convert(meal_time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(meal_time):

    hours, minutes = meal_time.split(":")
    time = round((float(hours) + (float(minutes))/60), 2)
    return time
    #print(time)


if __name__ == "__main__":
    main()