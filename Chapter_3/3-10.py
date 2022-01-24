dbz = []
dbz.append("Goku")
dbz.insert(1, "Vegita")
dbz.insert(2, "Gohan")
print(dbz)
print(f"Length of list = {len(dbz)}")
dbz.sort()
print(dbz)
dbz.sort(reverse=True)
print(dbz)

print(sorted(dbz, reverse=True))
print(dbz)
