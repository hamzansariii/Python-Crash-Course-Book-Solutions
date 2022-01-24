poll = {}

while True:
    name = input("What is your name : ")
    place = input("Where would you like to visit :")
    poll[name] = place
    new = input("Do you wanna enter more name?(yes/no)")
    if new == 'yes':
        continue
    else:
        break

print(poll)
for i, p in poll.items():
    print(i, '=', p)
