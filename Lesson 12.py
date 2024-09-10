import random

# l = 10 # int(input("len = "))
# list4 = [random.randint(0, 10) for i in range(l)]
# print(list4)
# for i in range(l//2):
#     list4[i], list4[l-1-i] = list4[l-1-i], list4[i]
#     # T = list4[i]
#     # list4[i] = list4[l-1-i]
#     # list4[l-1-i] = T
#
# print(list4)

# T = A
# A = B
# B = T

#list4.sort()
#list4.insert(2, 999)
#print(list4.index(9, 0,5))
#print(list4.count(9))
# list4.append(999)
# list4.pop(2)
# list4.remove(5)
# list4.reverse()

#print(list4)


# maxElem = list4[0]
# minElem = list4[0]
# iMax = 0
# iMin = 0
# for i in range(0, len(list4)):
#     if list4[i] > maxElem:
#         maxElem = list4[i]
#         iMax = i
#     if list4[i] < minElem:
#         minElem = list4[i]
#         iMin = i
# #print(maxElem, iMax)
# #print(minElem, iMin)
# s = 0
# if iMin < iMax:
#     a = iMin
#     b = iMax
# else:
#     a = iMax
#     b = iMin
# for i in range(a+1, b):
#     s += list4[i]

#print(s)


# iMax = list4.index(max(list4))
# iMin = list4.index(min(list4))

# Дан целочисленный массив размера N, не содержащий одинаковых
# чисел. Проверить, образуют ли его элементы арифметическую прогрессию

# a0 = 3
# d = 4
#
# l = 10 # int(input("len = "))
# list4 = [random.randint(0,9) for i in range(l)]
# #list4 = [a0 + i*d for i in range(l)]
# print(list4)
#
# a0 = list4[0]
# d = list4[1] - list4[0]
# isProgress = True
# for i in range(1, l-1):
#     if list4[i+1] - list4[i] == d:
#         continue
#     else:
#         isProgress = False
#         break
#
# print(isProgress)
# 3 5 7 9 11


l = 24 # int(input("len = "))
list4 = [random.randint(10,30) for i in range(l)]
print(list4)

list5 = []

# maxT = abs(list4[1] - list4[0])
# h = 0
# for i in range(1, l-1):
#     if abs(list4[i+1]-list4[i]) > maxT:
#         maxT = abs(list4[i+1]-list4[i])
#         h = i
# print(h)

