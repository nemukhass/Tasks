# a = int(input("vvedite chislo"))
# print(a,a*2)
# a = 46
# b = 6
# print(a,b*5)
# a = (5,"F","Привет",90.2)
# b = ("67")
# frozenset(b)
# print(a[2])
# a = (input("vvedite 4 znacnoe chislo"))
# b = list(a)
# for i in b:
#     print(i)
# a = input("vawe imya")
# b = input("vawa familiya")
# c = input("skolko vam let")
# print(a,b,c)
# a = int(input("vvedite 1 chislo"))
# b = int(input("vvedite 2 chislo"))
# c = int(input("vvedite 3 chislo"))
# print(a+b+c)
# print(a+b-c)
# print(a-b-c)
# a = int(input("vvedite 1 chislo"))
# b = float(input("vvedite 2 chislo"))
# c = input("vvedite 3 chislo")
# print(a,b,c)
# a = int(input("vvedite 1 chislo"))
# b = int(input("vvedite 2 chislo"))
# c = int(input("vvedite 3 chislo"))
# print(a+b+c)
# a = int(input("zaregayte parol"))
# b = int(input("povtorite parol"))
# if a == b:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
# a = int(input("vvedite 1 chislo"))
# b = int(input("vvedite 2 chislo"))
# c = input("viberite znak: +-*/")
# if c == "+":
#     print(a+b)
# if c == "-":
#     print(a-b)
# if c == "*":
#     print(a*b)
# if c == "/":
#     print(a/b)
# print("Hello World!")
# a = 5
# b = 10
# print("peremenniye v pitone i ispolzuyutsa chtobi xranit danniye kajdaya "
#       "peremena immet svoy tip ispolzovaniy naprimer ", a,b
#       )
# def proverka():
#     a = (int(input("введите 1 число")))
#     b = (int(input("введите 2 число")))
#     for i in range(a,b):
#         if i %2 == 0:
#             print(f'четное {i}')
#         elif i %2 == 1:
#             print(f'нечетное {i}')
# proverka()
# print("Циклы — базовый инструмент программирования на Python. "
#       "С их помощью разработчики могут быстро выполнять повторяющиеся действия,"
#       " автоматизируя процесс. В каждом цикле есть условие и блок кода, которые выполняются,"
#       " пока условие истинно. С помощью циклов for можно итерировать"
#       " коллекции данных, выполняя преобразования.")
# print("s pomowyu spiskov v pitone mojno dobavlyat, izmenyat, udalyat danniye")
# print("Функция — это блок кода, который запускается только при ее вызове."
#       " В функцию можно передавать данные, называемые параметрами."
#       " В результате функция может возвращать данные.")
print("Обработка исключений в Python позволяет управлять ошибками во время выполнения "
      "программы. Основные конструкции:try:"
      " Код, который может вызвать исключение.except: Обработка исключения.else: Код,"
      " выполняемый, если исключения не было.finally: Код, выполняемый всегда.Пример")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
else:
    print("Результат:", result)
finally:
    print("Конец блока")
try:
    value = int(input("Введите число: "))
    result = 10 / value
except ValueError:
    print("Это не число")
except ZeroDivisionError:
    print("Деление на ноль невозможно")