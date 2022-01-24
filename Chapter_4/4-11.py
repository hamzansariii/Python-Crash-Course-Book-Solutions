pizza = ["cheese Pizza", "peparroni pizza", "macaroni pizza"]
friend_pizza = pizza[:]
pizza.append('Pinapple pizza')
friend_pizza.append('thin crust pizza')
print(f'Original list {pizza}')
print(f"Friend's list {friend_pizza}")

print("\nMy favorite pizzas are ")
for i in pizza:
    print(i)

print("\nMy friends favorite pizza are ")
for i in friend_pizza:
    print(i)
