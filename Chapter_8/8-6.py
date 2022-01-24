def city_country(country, city):

    return f'"{country},{city}"'


while True:
    value1 = input("Enter Country name : ")
    value2 = input("Enter name of that country's city : ")
    value3 = city_country(value1, value2)
    print(value3)
