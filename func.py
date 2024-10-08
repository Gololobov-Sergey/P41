def printLine():
    for i in range(50):
        print("*", end='')
    print()


def Sum(a, b):
    c = a + b
    return c


def isEven(a):
    return a % 2 == 0

def isPositive(a):
    return a > 0

# sum list
def sum_list(list_):
    result = 0
    for elem in list_:
        result += elem
    return result

# Напишіть функцію, яка повертає максимальне з
# чотирьох чисел. Числа передаються як параметри.

def max4(a,b,c,d):
    max_elem = a
    if b > max_elem:
        max_elem = b
    if c > max_elem:
        max_elem = c
    if d > max_elem:
        max_elem = d
    return max_elem


# Напишіть функцію, яка перевіряє, чи є число простим.
# Число передається як параметр. Якщо число просте потрібно
# повернути з методу true, в іншому разі — false.

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



# Напишіть функцію, яка перевіряє, чи є шестизначне
# число "щасливим". Число передається як параметр.
# Якщо число щасливе потрібно повернути з функції true,
# якщо ні — false.


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def fact_r(n):
    if n == 1:
        return 1
    return n * fact_r(n-1)

def number(n):
    if n == 0:
        return
    print(n, end=' ')
    number(n-1)

def num1(n):
    if n > 1:
        num1(n-1)
    print(n, end=' ')

def sum2(a, b):
    if a == b:
        return b
    return a + sum2(a+1, b)


def count(n):
    if n == 0:
        return 0
    return n % 10 + count(n // 10)


def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)