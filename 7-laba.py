# student_info = {
#     "Имя": "Пернебай",
#     "Фамилия": "Алихан",
#     "Возраст": "19",
#     "Город": "Алматы",
#     "Университет": "Сатпаев",
#     "Факультет": "ИАиТИ",
#     "Специальность": "Computer Science",
#     "Средний балл": 5,
#     "Курсы": ["Функциональное программирование"]
# }
# def print_keys(dict):
#     print("Данный:")
#     for key in dict.keys():
#         print(key)

# print_keys(student_info)
# def print_values(dict):
#     print("Данный:")
#     for value in dict.values():
#         print(value)

# print_values(student_info)
# def print_items(dict):
#     print("Полный Резюме:")
#     for item in dict.items():
#         print(item)

# print_items(student_info)





countries = {
    "Казахстан": ["Іле", "Сырдария", "Нура"],
    "Корея": ["Кан", "Йонсанган", "Кымган"],
    "Туркия": ["Евфрат", "Гедис" , "Мурат"]
}
def find_river_country(river, countries):
    for country, rivers in countries.items():
        if river in rivers:
            return country
    return None

rivers = ["Кан", "Іле", "Гедис"]
for river in rivers:
    country = find_river_country(river, countries)
    if country:
        print(f"Река {river} орналасқан {country}.")
    else:
        print(f"Река туралы {river} информация жоқ.")
def find_river(river, countries):
    for country, rivers in countries.items():
        if river in rivers:
            return True
    return False

river_name = input("Река аты: ")
if find_river(river_name, countries):
    print(f"{river_name} ")
else:
    print(f"{river_name} ")

    country_name = input("Ел аты: ")
if country_name in countries:
    countries[country_name].append(river_name)
else:
    countries[country_name] = [river_name]

print(f"Сөздік қосылған: {countries}")




# commentators = {}

# while True:
#     input_string = input()
#     if input_string == "":
#         break
#     name, comment = input_string.split(": ")
#     if name not in commentators:
#         commentators[name] = None

# print(len(commentators))
