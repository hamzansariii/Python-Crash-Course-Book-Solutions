

class ElectricCar:
    def __init__(self, battery_size=450, battery_capacity=100):
        self.battery_capacity = battery_capacity
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size <= 500:
            range = 500
        elif self.battery_size > 500:
            range = 1000

        print(f"Battery Size : {range}")
        print(f"Battery Capacity : {self.battery_capacity}")


electric_car1 = ElectricCar(676, 56)
electric_car1.get_range()
