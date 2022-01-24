from random import choices

unit = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e')
chosen_list = []


def get_winning_ticket():
    for i in range(4):
        a = choices(unit, 5)
        chosen_list.append(a)

    chosen_string = f"{chosen_list[0]}{chosen_list[1]}{chosen_list[2]}{chosen_list[3]}"
    print(f"The winning lottery code is : {chosen_string}")


get_winning_ticket()
