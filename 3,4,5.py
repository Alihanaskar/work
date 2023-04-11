
#3:
from functools import reduce

my_list = [1, 2, 3, 4, 5]

# пример использования функции map
squared_list = list(map(lambda x: x ** 2, my_list))
print(squared_list)

# пример использования функции filter
even_list = list(filter(lambda x: x % 2 == 0, my_list))
print(even_list)

# пример использования функции reduce
product = reduce(lambda x, y: x * y, my_list)
print(product)

# #4:
# def delivery_cost(street, price):
#     if "Аль-Фараби" in street or "Саина" in street or "Ташенова" in street or "Достык" in street:
#         if price < 10000:
#             return 500
#         else:
#             return 0
#     else:
#         if price < 10000:
#             return 1000
#         else:
#             return 1000

# print(delivery_cost('Достык 36', 100000))

# #5:
# def compose(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# def f(x):
#     return x * 2

# def g(x):
#     return x + 1

# h = compose(f, g)

# result = h(3)
# print(result) #result:8

# #Yernur

# #Nargiza
