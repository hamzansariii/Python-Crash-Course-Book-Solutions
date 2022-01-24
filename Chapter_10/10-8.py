

try:
    with open('cats.txt') as ob_cats:
        content1 = ob_cats.read()

    with open('dogs.txt') as ob_dogs:
        content2 = ob_dogs.read()

except FileNotFoundError:
    print("File is not present in  the current folder")

else:
    print(content1)
    print(content2)
