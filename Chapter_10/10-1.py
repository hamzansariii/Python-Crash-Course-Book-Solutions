
file_name = "learning_python.txt"

with open(file_name) as txt_file:
    content = txt_file.read()
    print(content)

with open(file_name) as helllo:
    for i in helllo:
        print(i.rstrip())


with open(file_name) as new_file:
    new = new_file.readlines()

print(new)
for i in new:
    print(i.rstrip())
