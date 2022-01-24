river = {'Egypt': 'Nile', "ondia":
         "Ganga", "India": "Yamuna"}
for i, p in river.items():
    print(p, " river flows in ", i)

for i in river.keys():
    print("rivers\n", i)


for p in river.values():
    print("country\n", p)

for i in river.keys():
    value = river[i]
    print(i, '=', value)
