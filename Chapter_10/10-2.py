

with open("learning_python.txt") as new:
    for i in new:
        item = i.replace('python', 'c')
        print(item.rstrip())
