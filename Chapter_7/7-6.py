flag = True
while flag:
    age = int(input("Enter Your Age : "))
    if age <= 3:
        print("price = free")
    elif age > 3 and age <= 12:
        print("price = 10$")
    elif age > 12:
        print("price = 15$")
    nah = input("Do you want to quit(yes/no) : ")
    if nah == 'no':
        continue
    elif nah == 'yes':
        flag = False
