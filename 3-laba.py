# i = 5
# while i < 15:
#     print(i)
#     i = i + 2

# for i in 'hello world':
#     print(i * 2, end='')


# for number in range(5,15,2) :  

#     print("Я число : "+str(number))

# import random
 
# number = random.randint(20, 35)  # значение от 20 до 35
# print(number)

# import random
 
# number = random.random()  # значение от 0.0 до 1.0
# print(number)
# number = random.random() * 100  # значение от 0.0 до 100.0
# print(number)


# import random
 
# number = random.randrange(10)  # значение от 0 до 10 не включая
# print(number)
# number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
# print(number)
# number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
# print(number)

# names = ['Alikhan', 'Pernebai', 'Askaruly']
# for index, value in enumerate(names):
#     print(f'{index}: {value}')

# 1 esep

# A = int(input("A: "))
# B = int(input("B: "))

# if A < B:
#     for i in range(A, B + 1):
#         print(i)


# 2-esep

# A = int(input("A: "))
# B = int(input("B: "))

# if A < B:
#     for i in range(A, B + 1):
#         print(i)
# else:
#     for i in range(A, B - 1, -1):
#         print(i)

# 3 есеп

a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(a%2, end=' ')