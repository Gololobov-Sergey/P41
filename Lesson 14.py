import random
import string

st1 = "mama PAPA detka"
st2 = "papa"
# print(st1)
#
# for c in st1:
#     print(c)
#
#
# st3 = st1 + st2
# print(st3)
# print(st2 * 3)
# print("*" + str(30))

# print(st1.index("p", 6, 10))
# print(st1.count("papa"))
#print(st1.split("papa"))
# print(st1.find(" "))
# print(st1.rfind(" "))
# print(st1.startswith("m"))
# print(st1.endswith("ka"))
# st3 = st1.replace("a", "o", 2)
# st4 = st3.replace("o", "a", 2)
# print(st4)
# print(st1.lower())
# print(st1.upper())
# print(st1.title())
# print(st1.capitalize())
# print(st1.ljust(80), 234234)
# print(st1.center(80), 234234)
# print(st1.rjust(80), 234234)
# print(" ".isspace())
#
# l = [1,2,3,4,5]
# print(l)
# # for i in l:
# #     print(i, end=", ")
#
#
# print(", ".join([str(i) for i in l]))
# a = 3.14
# print(f"Number {a}")


# st = "Serhiy Gololobov"
# i = st.find(' ')
# st1 = st[i+1:] + " " + st[0:i]
# print(st1)
#
# st2 = st.split()
# st2.reverse()
# print(" ".join(st2))

# print(" ".join(st.split().reverse()))

# Дана строка, изображающая двоичную запись целого положительного
# числа. Вывести строку, изображающую десятичную запись этого же числа.

# 1001110101
# 101

# d = input()
# l = len(d)
# m = 0
# i = 0
# while(i < l):
#     m += int(d[i]) * 2**(l-1-i)
#     i += 1
# print(m)
#
# m = sum([int(d[i])*2**(len(d)-1-i) for i in range(len(d))])
# print(m)
#
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.ascii_uppercase)


# s = string.digits + string.ascii_letters
# l = [i for i in s]
# random.shuffle(l)
# password = "".join([random.choice(l) for _ in range(8)])
# print(password)
#
#
# st = "iuoeirtuoerit"
# for i in range(len(st)):
#     print(" "*i*3, st[i], sep='')


# st = "А роза упала на лапу Азора"
# st1 = st.replace(" ", "").lower()
# flag = True
# for i in range(len(st1)//2):
#     if st1[i] != st1[len(st1)-1-i]:
#         flag = False
#         break
# print(flag)

# l = [1,2,3,4,56]
# l2 = [4,1]
#
# print(l2[0] in l)