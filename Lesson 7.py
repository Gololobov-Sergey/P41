# import turtle
# import random
# # Fullscreen the canvas
# screen = turtle.Screen()
# screen.setup(1.0, 1.0)
#
# # Begin!
# t = turtle.Turtle()
# t.speed(100)
#
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# t.penup()
# for c in range(60):
#   t.color(colors[c%6])
#   #t.circle(random.randint(50, 100))
#   t.goto(random.randint(-400, 400), random.randint(-200, 200))
#   t.left(360/120)
#   t.pendown()
#   for j in range(5):
#     t.forward(20)
#     t.left(144)
#   t.penup()
# screen.mainloop()


# x1 = int(input("Число 1: "))
# x2 = int(input("Число 2: "))
# x3 = input("Действие: ")
#
# match x3:
#     case "+": result = x1 + x2
#     case "-": result = x1 - x2
#     case "*": result = x1 * x2
#     case "/": result = x1 / x2
#     case _:
#         print("Неправильно")
#
# if result != None:
#     print(result)



# Дано целое число в диапазоне 1–7. Вывести строку — название дня не-
# дели, соответствующее данному числу (1 — «понедельник», 2 — «втор-
# ник» и т. д.).

# w = int(input('1-7:'))
# match w:
#     case 1: print('понедельник')
#     case 2: print('вторник')
#     case 3: print('среда')
#     case 4: print('четверг')
#     case 5: print('пятница')
#     case 6: print('суббота')
#     case 7: print('воскресенье')
#     case _: print('error')


# Даны два целых числа: D (день) и M (месяц), определяющие правиль-
# ную дату невисокосного года. Вывести значения D и M для даты, следую-
# щей за указанной.

# 4 6
# 5 6
#
# 31 5
# 1 6
#
# 31 12
# 1 1

# d = int(input("D: "))
# m = int(input("M: "))
#
# match m:
#     case 4, 6, 9, 11: dmax = 30
#     case 2:           dmax = 28
#     case _:           dmax = 31

# if m == 4 or m == 6 or m == 9 or m == 11:
#     dmax = 30
# elif m == 2:
#     dmax = 28
# else:
#     dmax = 31

# d += 1
# if d > dmax:
#     d = 1
#     m += 1
# if m == 13:
#     m = 1
#
# print(d, m)

# Даны два целых числа: D (день) и M (месяц), определяющие правиль-
# ную дату невисокосного года. Вывести значения D и M для даты, предше-
# ствующей указанной.


# D = int(input("Введите D: "))
# M = int(input("Введите M: "))
#
# D -= 1
# if D == 0:
#     M -= 1
#     match M:
#         case 4, 6, 9, 11: D = 30
#         case 2:           D = 28
#         case _:           D = 31
#
# if M == 0:
#     M = 12
#
# print(D, M)
