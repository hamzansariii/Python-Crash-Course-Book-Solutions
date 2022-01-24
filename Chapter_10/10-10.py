
with open("gutenberg.txt") as ob:
    new = ob.read()
    new1 = new.lower()
    print(new1.count(" the "))
