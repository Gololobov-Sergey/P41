# a = 5
# while a >= 10:
#     print(a)
#     a += 1



# a = int(input("a = "))
# b = int(input("b = "))
# if a < b:
#     while a <= b:
#         print(a)
#         a += 1
# else:
#     while a >= b:
#         print(a)
#         a -= 1

# a = int(input("a = "))
# b = int(input("b = "))
# c = 0
# while a > b:
#     a -= b
#     c += 1
# print(a)
# print(c)


# Дано целое число N (> 0). Если оно является степенью числа 3, то вы-
# вести True, если не является — вывести False.

# n = int(input("n = "))
# k = 1
# while k < n:
#     k *= 3
# if n == k:
#     print(True)
# else:
#     print(False)


# Дано целое число N (> 0), являющееся некоторой степенью числа 2:
# N = 2^K . Найти целое число K — показатель этой степени.

# n = int(input("n = "))
# k = 1
# c = 0
# while k < n:
#     k *= 2
#     c += 1
# print(c)


# Дано число A (> 1). Вывести наибольшее из целых чисел K, для кото-
# рых сумма 1 + 1/2 + ... + 1/K будет меньше A, и саму эту сумму.

# n = int(input("n = "))
# k = 1
# s = 0
# while s < n:
#     s += 1/k
#     k += 1
# print(k-1)
# print(s-1/k)


# Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км.
# Каждый следующий день он увеличивал длину пробега на P процентов от
# пробега предыдущего дня (P — ціле, 0 < P < 50). По данному P
# определить, после какого дня суммарный пробег лыжника за все дни пре-
# высит 200 км, и вывести найденное количество дней K (целое) и суммар-
# ный пробег S (вещественное число).

# s = 10
# sp = 10
# k = 1
# p = 50
# while s <= 200:
#     sp = sp + sp*p/100
#     s += sp
#     k += 1
#
# print(k)
# print(s)



n = int(input("n = "))
s = 0
k = 0
while n > 0:
    r = n % 10
    s += r
    n //= 10
    k += 1

print(s)
print(k)

# import time
#
# a = 1
# while True:
#     while a < 10:
#         print(".", end='')
#         a += 1
#         time.sleep(0.5)
#     while a >=1:
#         print("\b", end="")
#         time.sleep(0.5)
#         a -= 1
