# # кортеж (tuple) жасау
# tuple_1 = (2, 1, 4, 3)

# # жұмыс (set) жасау
# set_1 = {1, 2, 3, 4}

# # len() функциясын қолдану
# print(len(tuple_1))
# print(len(set_1))

# # sorted() функциясын қолдану (set-терді сұрыптау мүмкін емес)
# print(sorted(tuple_1))

# # count() функциясын қолдану
# tuple_2 = (1, 2, 3, 4, 1, 2, 3, 1)
# print(tuple_2.count(1))

# # union() функциясын қолдану
# set_2 = {3, 4, 5, 6}
# print(set_1.union(set_2))

# # intersection() функциясын қолдану
# print(set_1.intersection(set_2))




# import random

# def fill_tuple(start, end, length):
#     return tuple(random.randint(start, end) for _ in range(length))

# tuple_1 = fill_tuple(0, 5, 10)
# tuple_2 = fill_tuple(-5, 0, 10)

# tuple_3 = tuple_1 + tuple_2

# count_zeros = tuple_3.count(0)

# print("Tuple 1: ", tuple_1)
# print("Tuple 2: ", tuple_2)
# print("Tuple 3: ", tuple_3)
# print("Number of zeros in Tuple 3: ", count_zeros)


# import random
# my_tuple = (1, (42, (3.14, ((3+2j), ('Конечная строка', ()))))) 
# new = my_tuple[1][1][1][0] 
# print(new) 

# # Вводим имена студентов через пробел
# names_input = input("Введите имена студентов через пробел: ")

# # Создаем кортеж из имен студентов
# names_tuple = tuple(names_input.split())

# filtered_names = filter(lambda name: "ал" in name, names_tuple)

# print(" ".join(filtered_names))


from transliterate import translit

# Вводим текст на казахском языке
text = input("Введите текст на казахском языке: ")

# Переводим текст в латиницу
latin_text = translit(text, 'kk', reversed=True)

# Выводим результат
print(latin_text)