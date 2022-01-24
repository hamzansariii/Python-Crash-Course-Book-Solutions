new = ['Hamza', 'Shakeel', 'Zaid']
print(f"Sorry Hamza will not come")
del new[0]
new.insert(0, 'Ayesha')
for i in new:
    print(f"You are invited {i}".title())
print("Hey I have got bigger dining table I'll invite 3 more people")
new.insert(0, 'Fatima')
new.insert(2, "Naheed")
new.append("anyone")
for i in new:
    print(f"You are invited {i}")

print('You can invite only 2 people')

a = new.pop(0)
print(f"Sorry {a}")
b = new.pop(0)
print(f"Sorry {b}")
c = new.pop(0)
print(f"Sorry {c}")
d = new.pop(0)
print(f"Sorry {d}")
e = new.pop(0)
print(f"Sorry {e}")
del new[0]
print(new)
