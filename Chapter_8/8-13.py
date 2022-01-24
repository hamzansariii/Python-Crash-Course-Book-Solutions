
def build_profile(first, last, age, profile={}):
    profile['First_name'] = first
    profile['last_name'] = last
    profile['age'] = age
    for i, p in profile.items():
        print(f"{i}={p}")


while True:
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    age = input("Enter your age : ")
    if first_name == "quit":
        break
    build_profile(first_name, last_name, age)
