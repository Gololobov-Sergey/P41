# not
# > , < , == , != , <= , >=,
# or(+), and(*), ^(xor)

'''a = 5
b = 4
c = not (a == (not b))
print(c)
print(True or True)
print(False or True)
print(True or False)
print(False or False)

print(True ^ True)

print()
print(True and True)
print(False and True)
print(True and False)
print(False and False)'''

'''a = int(input("a = "))
res = a > 0
print(res)'''


# Дано целое число A. Проверить истинность высказывания: «Число A
# является нечетным».

'''a = int(input("a = "))
res = a % 2 == 1
print(res)'''

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A > 2 и B ≤ 3».

'''a = int(input("a = "))
b = int(input("b = "))
res = a > 2 and b <= 3
print(res)'''


# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Справедливы неравенства A ≥ 0 или B < –2».

'''a = int(input("a = "))
b = int(input("b = "))
res = a >= 0 or b < -2
print(res)'''


# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Справедливо двойное неравенство A < B < C».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
res = a < b < c
print(res)'''


# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Число B находится между числами A и C».

'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
res = a < b < c or a > b > c
print(res)'''

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Каждое из чисел A и B нечетное».

# a = int(input("a = "))
# b = int(input("b = "))
# res = a % 2 == 1 and b % 2 == 1
# print(res)


# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Хотя бы одно из чисел A и B нечетное».


# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Ровно одно из чисел A и B нечетное».

# a = int(input("a = "))
# b = int(input("b = "))
# res = a % 2 == 1 and b % 2 == 0 or a % 2 == 0 and b % 2 == 1
# print(res)

# Даны два целых числа: A, B. Проверить истинность высказывания:
# «Числа A и B имеют одинаковую четность».

# a = int(input("a = "))
# b = int(input("b = "))
# res = a % 2 == b % 2
# print(res)


# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Каждое из чисел A, B, C положительное».

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# res = a > 0 and b > 0 and c > 0
# print(res)

# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Ровно одно из чисел A, B, C положительное».


#res = ((a > 0) + (b > 0) + (c > 0)) == 2


# Даны три целых числа: A, B, C. Проверить истинность высказыва-
# ния: «Ровно два из чисел A, B, C являются положительными».

#res = ((a > 0) + (b > 0) + (c > 0)) == 2

# Дано целое положительное число. Проверить истинность высказы-
# вания: «Данное число является четным двузначным».

#res = a >= 10 and a < 100 and a % 2 == 0

# Дано целое положительное число. Проверить истинность высказы-
# вания: «Данное число является нечетным трехзначным».

#res = a >= 100 and a < 1000 and a % 2 == 1

# Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара совпадающих».

#res = a == b or b == c or c == a


# Проверить истинность высказывания: «Среди трех данных целых
# чисел есть хотя бы одна пара взаимно противоположных».

a = 5
b = -5

a == -b