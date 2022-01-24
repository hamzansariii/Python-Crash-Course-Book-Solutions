
from os import name


filename = "guest_book.txt"

while True:
    name = input("Enter your name : ")
    name_string = f"{name} added to the guest book."
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as ob_name:
            ob_name.write(name_string + '\n')
