# for i in range(20, 40, 2):
#     print(i)


# Даны два целых числа A и B (A < B). Вывести в порядке возрастания все
# целые числа, расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.

# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b+1):
#     print(i, end=' ')
# print()
# print(b-a+1)


# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1,
# 2, ..., 10 кг конфет.

# c = float(input("c = "))
# for i in range(1, 11):
#     print(i, "кг - коштує", round(c*i, 2), "грн")


# m = int(input("Скількі є магазинів: "))
# s = 0
# for i in range(1, m+1):
#     print("Введіть кількість холодильників в магазині №", i, ": ", end='')
#     h = int(input())
#     if h > 100:
#         s += 1
# print("Всього", s)


#s = 11 + 22 + 33 + ... +nn

# import math
# print(math.pow(10, 3))
# print(10**3)

# n = int(input("n = "))
# s = 0
# for i in range(1, n+1):
#     k = 0
#     m = i
#     while m > 0:
#         k += 1
#         m //=10
#     s1 = i*(10**k) + i
#     s += s1
#     print(s1, end=' ')
# print()
# print(s)

# n = 25
# s = 1.1 + 1.2 + 1.3 + .... + 1.25

# n = int(input(' n = : '))
# s = 0
# for i in range(0, n+1):
#      k = 0
#      m = i
#      while m > 0:
#           k += 1
#           m //= 10
#      s1 = i * 0.1**k
#      s += s1
#      print(round(s1+1 , k) , end=" ")

s = 0
for i in range(10000, 100000):
    m = i
    k = 0
    while m > 0:
        r = m % 10
        if r == 5:
            k += 1
        m //= 10
    if k == 3 and i % 9 == 0:
        print(i, end=' ')
        s += 1
print()
print(s)