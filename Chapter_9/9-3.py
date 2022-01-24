class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(
            f"First_Name : {self.first_name}\nLast_Name : {self.last_name}\nAge : {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


user1 = User('Hamza', 'Ansari', 20)
user2 = User('Yousuf', 'Ansari', 14)
user3 = User('Maaz', "Ansari", 15)


user1.describe_user()
user1.greet_user()
