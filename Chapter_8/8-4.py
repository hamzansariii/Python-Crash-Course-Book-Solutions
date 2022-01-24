
def my_shirt(list1, text1, a, b):
    while list1:
        hey = list1.pop()
        print(f"Shirt Size={hey} and Text={text1}")

    print(f'Size={a} and Text={b}')


list1 = ['Larger', 'Medium']
text1 = "I love Python"
size = input("What size You Want : ")
text2 = input("What text do you want : ")
my_shirt(list1, text1, size, text2)
