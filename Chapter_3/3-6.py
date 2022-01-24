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
