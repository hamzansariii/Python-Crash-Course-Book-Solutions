class User:
    def __init__(self, first_name, last_name, age, login_attempt=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = login_attempt

    def describe_user(self):
        print(
            f"First_Name : {self.first_name}\nLast_Name : {self.last_name}\nAge : {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


user1 = User('Hamza', 'Ansari', 20)
user2 = User('Yousuf', 'Ansari', 14)
user3 = User('Maaz', "Ansari", 15)


user1.describe_user()
user1.greet_user()
print("Login Attempt : ", user1.login_attempt)
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print("Login Attempt : ", user1.login_attempt)
user1.reset_login_attempt()
print("Login Attempt : ", user1.login_attempt)
