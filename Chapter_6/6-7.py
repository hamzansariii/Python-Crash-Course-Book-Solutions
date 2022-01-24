person1 = {'first_name': 'Hamza',
           'last_name': 'Ansari', 'city': 'Mumbra', 'age': 20}
person2 = {'first_name': 'Faisal',
           'last_name': 'Ansari', 'city': 'Kurla', 'age': 14}
person3 = {'first_name': 'Yousuf',
           'last_name': 'Ansari', 'city': 'Bhiwandi', 'age': 14}

people = []
people.append(person1)
people.append(person2)
people.append(person3)
print(people)

print("\n", people[0])
print("\n", people[1])
print("\n", people[2], "\n")

for i, p in people[0].items():
    print(i, "=", p, "\n")
for i, p in people[1].items():
    print(i, "=", p, "\n")
for i, p in people[2].items():
    print(i, "=", p, "\n")
