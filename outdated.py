months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("date: ")
    if "/" in date or "," in date:
        # handling USA date format
        if "/" in date:
            parts = date.split("/")
            if len(parts) == 3:
                month, day, year = parts
                try:
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    if month > 12 or month < 1 or day < 1 or day > 31:
                        date = input("date: ")
                    else:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
                except ValueError:
                    pass

        # handling date format with full month name
        else:
            parts = date.split(" ")
            if len(parts) == 3:
                month, day, year = parts
                month = month.capitalize()
                if month in months:
                    try:
                        month = months.index(month) + 1
                        day = int(day.strip(","))
                        year = int(year)
                        if month > 12 or month < 1 or day < 1 or day > 31:
                            date = input("date: ")
                        else:
                            print(f"{year:04d}-{month:02d}-{day:02d}")
                            break
                    except ValueError:
                        pass
    else:
        date = input("date: ")