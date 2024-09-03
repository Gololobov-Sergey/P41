import math
import random

# R = int(input("R = "))
# r = int(input("r = "))
# h = int(input("h = "))
#
# k = 0
#
# for x in range(-R, R+1, h):
#     for y in range(-R, R+1, h):
#         l = math.sqrt(x*x + y*y)
#         if l > r and l < R:
#             k += 1
# print(k)


# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# list1 = [a, b, c]
#
# k = 0
# for i in range(3):
#     if list1[i] > 0:
#         k += 1
# print(k)


# list2 = [123, "mama", True, 3.14]
# print(list2)
#
# print(list2[1])
#
# for i in range(len(list2)):
#     print(list2[i])
#
# for i in list2:
#     print(i)

# k = 0
# list3 = [1,0,0,1,1,0,1,0,1,1]
# for i in list3:
#     if i == 0:
#         k += 1
# print(k)

l = int(input("len = "))
list4 = [random.randint(0, 9) for i in range(l)]
print(list4)