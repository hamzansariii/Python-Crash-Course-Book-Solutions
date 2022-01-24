
import json

file = 'fav_number.json'

with open(file) as ob:
    new = json.load(ob)


print(f"Your fav number was {new}")
