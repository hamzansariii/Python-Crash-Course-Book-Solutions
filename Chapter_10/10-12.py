

import json
from json.decoder import JSONDecodeError


def store_number():
    num = int(input("Enter your fav number"))
    with open("fav_number.json", 'w') as store:
        json.dump(num, store)


def get_number():
    with open("fav_number.json") as get:
        number = json.load(get)

    print(f"Your favourite number is {number}")


try:
    get_number()
except JSONDecodeError:
    store_number()
