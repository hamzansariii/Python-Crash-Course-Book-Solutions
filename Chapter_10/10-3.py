import json


name = input("Enter your name : ")
filename = 'guest_book.txt'
with open(filename, 'w') as user_name:
    json.dump(name, user_name)
