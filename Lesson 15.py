import random
from func import *


#
print(printLine)
printLine()
#
#
printLine()


print(Sum(3,6))


a = [random.randint(1,10) for i in range(10)]
print(a)
# s = sum_list(a)
# print(s)
#
# # b = 0
# # for i in a:
# #     if isPositive(i):
# #         b += 1
# # print(b)
#
#
# print(max4(3,6,43,6))

for i in a:
    if isPrime(i):
        print(i, end=', ')
print()

b=[i for i in a if isPrime(i)]
print(b)