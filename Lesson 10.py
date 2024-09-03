# n = 5
# for k in range(3):
#     for i in range(n-2+k):
#         for j in range(n-1-i+2-k):
#             print(" ", end=' ')
#         for j in range(2*i+1+2*k):
#             print("*", end=' ')
#         print()

# c = 0
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             h1 = h // 10
#             h2 = h % 10
#             m1 = m // 10
#             m2 = m % 10
#             s1 = s // 10
#             s2 = s % 10
#             if h1 == s2 and h2 == s1 and m1 == m2:
#                 print(f"{h1}{h2}:{m1}{m2}:{s1}{s2}")
#                 c += 1
# print(c)


n = 4
for i in range(10**(n-1), 10**n):
    s = 0
    m = i
    for k in range(n):
        r = m % 10
        s += r**n
        m //= 10
    if s == i:
        print(i)