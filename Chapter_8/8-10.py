def send_message(list1, list2=[]):
    for i in list1:
        list2.append(i)
    print(list1)
    print(list2)


msh = ['hi', 'bye', 'why']
send_message(msh)
