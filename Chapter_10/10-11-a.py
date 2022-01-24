import json

fav_number = int(input("Enter your fav number : "))

file = 'fav_number.json'

with open(file, "w") as fi:
    json.dump(fav_number, fi)
