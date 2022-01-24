sandwich_orders = ['cheese sandwich', 'pastrami', 'shezwan sandwich',
                   'pastrami', 'butter sandwich', 'pastrami']
finished_sandwich = []
print("Deli has run out of pastrami\n ")
while True:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
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
