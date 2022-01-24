sandwich_orders = ['cheese sandwich', 'shezwan sandwich', 'butter sandwich']
finished_sandwich = []

while True:
    order = sandwich_orders.pop()
    print(f"Your {order} is ready")
    finished_sandwich.append(order)
    if sandwich_orders == []:
        break
    else:
        continue

print(finished_sandwich)
for i in finished_sandwich:
    print(f"We have served {i} ")
