# Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние
# между ними S км. Определить расстояние между ними через T часов, если
# автомобили первоначально движутся навстречу друг другу.

'''v1 = int(input("V1 : "))
v2 = int(input("V2 : "))
s = int(input("S : "))
t = int(input("T : "))

s1 = abs(s - v1 * t - v2 * t)
print(s1)'''


# Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без на-
# ложений). найти количество отрезков B, размещенных на отрезке A.

'''a = int(input("a = "))
b = int(input("b = "))
print(a//b)
print(a%b)'''

'''a = int(input("a = "))
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
#print(a1, a2, a3)
b = a3*100 + a2*10 + a1
print(b)'''


# С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала суток.
'''n = int(input("n = "))
print(n//60)'''


# С начала суток прошло N секунд (N — целое). Найти количество
# полных часов, прошедших с начала суток.
'''n = int(input("n = "))
print(n//3600)'''


# С начала суток прошло N секунд (N — целое). Найти количество се-
# кунд, прошедших с начала последней минуты.
'''n = int(input("n = "))
print(n%60)'''


# С начала суток прошло N секунд (N — целое). Найти количество се-
# кунд, прошедших с начала последнего часа.
'''n = int(input("n = "))
print(n%3600)'''


# С начала суток прошло N секунд (N — целое). Найти количество
# полных минут, прошедших с начала последнего часа.
'''n = int(input("n = "))
print(n%3600//60)'''


# Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, ..., 6 — суббота. Дано целое число K, ле-
# жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было понедельником.
'''k = int(input("k = "))
print(k%7)'''


# Дни недели пронумерованы следующим образом: 0 — воскресенье,
# 1 — понедельник, 2 — вторник, ..., 6 — суббота. Дано целое число K, ле-
# жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было четвергом.
'''k = int(input("k = "))
print((k+3)%7)'''



# Дни недели пронумерованы следующим образом: 1 — понедельник,
# 2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, ле-
# жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было вторником.

k = int(input("k = "))
print(k%7+1)


# Дни недели пронумерованы следующим образом: 1 — понедельник,
# 2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, ле-
# жащее в диапазоне 1–365. Определить номер дня недели для K-го дня года,
# если известно, что в этом году 1 января было субботой.

k = int(input("k = "))
print(k%7+1)