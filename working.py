import re
import sys

def main():
    print(convert(input("Hours: ")))
    sys.exit(0)


def convert(s):
    if "AM" not in s and "PM" not in s and "to" not in s:
        sys.exit("ValueError")
    start, end = s.split(" to ")
#    print(start)
#    print(end)
    if matches := re.search(r"^(\d{1,2}):?(\d{2})?\s(AM|PM)$", start, re.IGNORECASE):
        hour_start = matches.group(1)
#        print(hour_start)
        minute_start = matches.group(2)
        if minute_start == None:
            minute_start = "00"
#        print(minute_start)
        if int(hour_start) > 12 or int(minute_start) > 59:
            sys.exit("ValueError")

        if "AM" in start and int(hour_start) < 12:
            start = hour_start.zfill(2)+":"+minute_start

        elif "AM" in start and int(hour_start) == 12:
            hour_start = "00"
            start = hour_start.zfill(2)+":"+minute_start
#            print(start)

        elif "PM" in start and int(hour_start) < 12:
            hour_start = int(hour_start) + 12
            hour_start = str(hour_start)
            start = hour_start.zfill(2)+":"+minute_start

        elif "PM" in start and int(hour_start) == 12:
            hour_start = 12
#            print(hour_start)
            start = hour_start.zfill(2)+":"+minute_start

        else:
            sys.exit("ValueError")
    else:
        sys.exit("ValueError")
    if matches := re.search(r"^(\d{1,2}):?(\d{2})?\s(AM|PM)$", end, re.IGNORECASE):
        hour_end = matches.group(1)
#        print(hour_end)
        minute_end = matches.group(2)
        if minute_end == None:
            minute_end = "00"
#        print(minute_end)
        if int(hour_end) > 12 or int(minute_end) > 59:
            sys.exit("ValueError")

        if "AM" in end and int(hour_end) < 12:
            end = hour_end.zfill(2)+":"+minute_end

        elif "AM" in end and int(hour_end) == 12:
            hour_end == "00"
            end = hour_end.zfill(2)+":"+minute_end

        elif "PM" in end and int(hour_end) < 12:
            hour_end = int(hour_end) + 12
            hour_end = str(hour_end)
            end = hour_end.zfill(2)+":"+minute_end

        elif "PM" in end and int(hour_end) == 12:
            hour_end = "12"
#            print(hour_start)
            end = hour_end.zfill(2)+":"+minute_end
#            print(end)
        else:
            sys.exit("ValueError")
        time = start+" to "+end
        return time
    else:
        sys.exit("ValueError")


if __name__ == "__main__":
    main()