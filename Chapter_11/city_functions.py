

def City_Country_Name(city_name, country_name, population=''):
    if population:
        name = f"{city_name},{country_name},{population}"
    else:
        name = f"{city_name},{country_name}"
    return name
