new = ['Hamza', 'Shakeel', 'Zaid']
print(f"Sorry Hamza will not come")
del new[0]
new.insert(0, 'Ayesha')
for i in new:
    print(f"You are invited {i}".title())
