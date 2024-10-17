from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet = Figlet()
    figlet_font = figlet.getFonts()
    chosen = random.choice(figlet_font)
    figlet.setFont(font = chosen)

    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--f":
        text = input("Input: ")
        figlet = Figlet()
        figlet_font =figlet.getFonts()
        chosen = sys.argv[2]
        if chosen not in figlet_font:
            sys.exit("Correct execution: python figlet.py or python figlet.py --f font")

        figlet.setFont(font = chosen)

        print(figlet.renderText(text))
    else:
        sys.exit("Correct execution: python figlet.py or python figlet.py --f font")

else:
    sys.exit("Correct execution: python figlet.py or python figlet.py --f font")
