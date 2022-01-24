
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


class Ten_Sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides=sides)
        self.sides = 10


class Twenty_Sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides=sides)
        self.sides = 20


player1 = Die()
player1.roll_die()


player1 = Ten_Sided_Die()
player1.roll_die()

player1 = Twenty_Sided_Die()
player1.roll_die()
