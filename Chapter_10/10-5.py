filename = 'poll.txt'

print("Enter 'quit' anytime to exit")


while True:
    name = input("Enter your name : ")
    name_string = f'Name : {name}'
    if name == 'quit':
        break
    lang = input("Enter your favourite language : ")
    lang_string = f"language : {lang}"
    if lang == 'quit':
        break

    reason = input(f"Why {lang} is your favourite language : ")
    reason_string = f"Reason : {reason}"
    if reason == 'quit':
        break

    with open(filename, 'a') as ob_name:
        ob_name.write('\n'+name_string+"\n")
        ob_name.write(lang_string+"\n")
        ob_name.write(reason_string+'\n')
