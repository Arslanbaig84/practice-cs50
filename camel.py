name = input("Name: ")
new_name = ""

for char in name:
    if char.isupper():
        new_name += "_" + char.lower()
    else:
        new_name += char


print(new_name)