import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'src="(.*?)"', s):
        http_link = matches.group(1)
        link = http_link.removeprefix("src=")
        link = link.strip('"')
        if "youtube" not in link:
            return None
        else:
            parts = link.split("embed")
            link = "https://youtu.be"+parts[1]
            return link


if __name__ == "__main__":
    main()