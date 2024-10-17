import inflect

p = inflect.engine()

#mylist = "mango, "

#mylist = mylist + p.join(("apple", "banana", "carrot"))
#print(mylist)
# "apple, banana, and carrot"

#mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

song = "Adieu, adieu, to "
mylist = []

while True:
    try:
        name = input("")
        mylist.append(name)
    except EOFError:
        song = song + p.join(mylist)
        print(song)
        break