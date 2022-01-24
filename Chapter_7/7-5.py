while True:
    age = int(input("Enter Your Age : "))
    if age <= 3:
        print("price = free")
    elif age > 3 and age <= 12:
        print("price = 10$")
    elif age > 12:
        print("price = 15$")
