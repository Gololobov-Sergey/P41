import random

from func import *


# print(Sum(10))
#
# printLine()
# printLine(20)
# printLine(30, '$')


def hello():
    print("Hello")

def goodbye():
    print("Goodbye")


def sum(a,b):
    return a + b

def diff(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def pow(a,b):
    return a**b

# oper = [sum, diff, mult, div, pow]
#
# a = int(input("a = "))
# b = int(input("b = "))
# op = int(input("1 Sum, 2 Diff, 3 Mult, 4 Div, 5 Pow : "))
# print(oper[op-1](a, b))


# message = [hello, goodbye]
#
# for f in message:
#     f()


# message[1]()

# message()
# message = goodbye
# message()



l = 30 # int(input("len = "))
list1 = [random.randint(10,999) for i in range(l)]
print(list1)
bubbleSort(list1, lastNumber)
print(list1)

# listP = []
# listN = []
# for el in list1:
#     if el % 2 == 0:
#         listP.append(el)
#     else:
#         listN.append(el)
#
# bubbleSort(listP)
# bubbleSort(listN)
# list1 = listP + listN
# print(list1)

print(f(1,2,3,4,5))