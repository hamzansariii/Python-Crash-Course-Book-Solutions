def make_car(car_manufacturer, car_model, **kwargs):
    info = {}
    info['Car_mafufacturer'] = car_manufacturer
    info['car_model'] = car_model
    for i, p in kwargs.items():
        info[i] = p

    for i, p in info.items():
        print(f"{i}={p}")


make_car('honda', 'cedan', color="black", rims="golden", horsepower="800")
