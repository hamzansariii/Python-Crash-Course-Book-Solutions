
try:
    no1 = int(input("Enter no 1 : "))
    no2 = int(input("Enter no 2 : "))
except ValueError:
    print("I need a number")
else:
    print(no1+no2)
