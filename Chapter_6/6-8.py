pet1 = {'Cat': 'Hamza'}
pet2 = {'Dog': 'Yousuf'}
pet3 = {'Rabbit': 'Faisal'}

animal = [pet1, pet2, pet3]

for i, p in animal[0].items():
    print(i, "=", p)

for i, p in animal[1].items():
    print(i, "=", p)

for i, p in animal[2].items():
    print(i, "=", p)
