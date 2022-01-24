class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"Restaurant_Name : {self.restaurant_name}")
        print(f"Cusine_Type : {self.cusine_type}")

    def open_restaurant(self):
        print("\nRestaurant is open!")


restaurant_1 = Restaurant("Udupi", "South Indian")

# only instances are used
print("Restaurant Name ", restaurant_1.restaurant_name)
print("cusine_type ", restaurant_1.cusine_type)

restaurant_1.open_restaurant()  # instance and methods both are used
restaurant_1.describe_restaurant()
