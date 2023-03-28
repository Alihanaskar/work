# print("Сколько бананов и ананасов для обезьян?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
 
# print("Сколько жуков и червей для ежей?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")
 
# print("Сколько рыб и моллюсков для выдр?")
# a = int(input())
# b = int(input())
# print("Всего", a+b, "шт.")






# class Student:
#     def __init__(self, name, cls):
#         self.name = name
#         self.cls = cls
#     def __str__(self):
#         return "ФИО: "+ self.name +" Класс: "+ self.cls

# studentList = []
# print("ФИО:")
# name = input()
# print("Класс")
# cls = input()    
# print()
# while True:
#     st = Student(name, cls)
#     studentList.append(st)
#     print("ФИО:")
#     name = input()
#     print("Класс")
#     cls = input()
#     print()
#     if name == '' and cls == '':
#         break

# #Вывод списка
# for student in studentList:
#         print(student)
# print()
# studentList.sort(key=lambda x: x.cls)
# #Вывод сортированного списка 
# for student in studentList:
#         print(student)






# s = 'HELLO WORLD'

# k1 = 0
# k2 = 0
# for i in s:
#     if('A'<i<'Z'):
#         k1+=1
#     if('a'<i<'z'):
#         k2+=1
# if(k1<k2):
#     if(s.islower()==True):
#         print('Already lower')
#     else:
#         print(s.lower())
# elif(k1>k2):
#     if(s.isupper()==True):
#         print('Already upper')
#     else:
#         print(s.upper())   




# a = input()
# b = input()
# print()

# while not(a.isdigit() and b.isdigit()):
#     a = input()
#     b = input()


# sum = int(a) + int(b)
# print(sum)