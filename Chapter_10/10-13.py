import json

filename = "username.json"


def get_user_name():
    with open(filename) as get:
        get_name = json.load(get)
    print(f"Username : {get_name}")


def store_user_name():
    name = input("Enter your name : ")
    with open(filename, 'w') as store:
        json.dump(name, store)


def greet_user():
    with open(filename) as greet:
        greet_name = json.load(greet)
    print('Hello, ', greet_name)


def cross_check():
    get_user_name()
    answer = input("Are you the correct user mentioned here?")
    if answer == 'yes':
        greet_user()

    if answer == 'no':
        store_user_name()
        greet_user()


cross_check()
