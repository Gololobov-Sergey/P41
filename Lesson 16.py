from func import *

print(fact_r(5))

number(5)
print()

num1(5)
print()

print(sum2(1, 10))
print(count(123))

# 1 1 2 3 5 8 13 21 34 55 89 ....
#
# F1 = 1, F2 = 1
# F(n) = F(n-1) + F(n-2)

F1 = 1
F2 = 1
n = int(input("n = "))
k = 2
while k < n:
    Fn = F1 + F2
    F2 = F1
    F1 = Fn
    k += 1

print(Fn)
print(fibo(n))