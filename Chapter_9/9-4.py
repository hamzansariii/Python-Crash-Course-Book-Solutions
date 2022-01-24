
class Restaurant:
    def __init__(self, restaurant_name, cusine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant_Name : {self.restaurant_name}")
        print(f"Cusine_Type : {self.cusine_type}")

    def open_restaurant(self):
        print("\nRestaurant is open!")

    def set_number_served(self):
        new_num_served = int(input("How many customers have been served : "))
        if new_num_served >= self.number_served:
            self.number_served = new_num_served

    def increment_number_served(self):
        while True:
            new_incre = int(input("New incremented number of customers : "))
            self.number_served += new_incre
            if new_incre == 0:
                break


res1 = Restaurant('Udupi', 'south_Indian', 9)
res1.open_restaurant()
res1.describe_restaurant()
print("Number of customer served : ", res1.number_served)
res1.increment_number_served()
print("Number of customer served : ", res1.number_served)
