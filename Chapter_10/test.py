
import json
filename = 'username.json'


def get_stored_data():
    with open(filename) as stored_username:
        username = json.load(stored_username)
    return username


def get_new_data():
    new_data = input("Enter your name : ")
    with open(filename, 'w') as new_name:
        json.dump(new_data, new_name)
    print("We will remember you ", new_name)
    return new_name


def greetuser():
    try:
        get_stored_data()
    except FileNotFoundError:
        new_name = get_new_data()
        print("Hello ", new_name)
    else:
        print("Hello ", get_stored_data())


greetuser()
