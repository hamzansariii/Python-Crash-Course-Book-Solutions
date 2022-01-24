
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


user2.describe_user()
user2.greet_user()


class Privilage():  # used in admin class
    def __init__(self):
        self.privilages = ["Can add post", "Can ban user",
                           "Can kick user", "Can add new members"]

    def show_privilages(self):
        print("Privilages:")
        for i in self.privilages:
            print(i)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priv = Privilage()

    def show_admin_privilage(self):
        print("Admin Privilage")
        for i in self.privilages:
            print(i)


admin1 = Admin("Hamza", "Ansari", 20)

admin1.describe_user()
admin1.priv.show_privilages()  # merging two classes methods
