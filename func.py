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

