# year = 2024
# f = open("text.txt", "w", encoding="utf-8")
# f.write("Слава Україні!\n")
# f.write("Hello Python 123123\n")
# f.write(str(year))
# f.close()
import random

# f = open("text.txt", "r")
# n = [int(i) for i in f.read().split()]
# f2 = open("tex2.txt", "w")
# for i in n:
#     if i % 2 == 0:
#         f2.write(str(i) + " ")
#
# f.close()
# f2.close()


# marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
# for l in marks:
#     l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

# print(marks)
#
# f = open("students.txt", "w", encoding="utf-8")
# for row in marks:
#     for el in row:
#         f.write(str(el) + ", ")
#     f.write("\n")
# f.close()

# marks = []
# f = open("students.txt", "r", encoding="utf-8")
# st = f.readlines()
# for el in st:
#     el = el.replace('\n', '').split(', ')
#     el.remove('')
#     for j in range(1, len(el)):
#         el[j] = int(el[j])
#     marks.append(el)
#
# print(marks)


# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# f = open("log.txt", "w")
# for i in range(10000):
#     f.write("192.168.0." + str(random.randint(100, 255)) + " " + week[random.randint(0,6)] + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + "\n")


f = open("log.txt", "r")
log = f.readlines()
logIP = []
for s in log:
    logIP.append(s.replace('\n', '').split())

IP = [el[0] for el in logIP]
print(len(IP))


uniqIP = set(IP)
# for ip in IP:
#     if ip not in uniqIP:
#         uniqIP.append(ip)

print(len(uniqIP))

maxCount = 0
maxIP = ''
for ip in uniqIP:
    count = IP.count(ip)
    if count > maxCount:
        maxCount = count
        maxIP = ip

print(maxIP, maxCount)