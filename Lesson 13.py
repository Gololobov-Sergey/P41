import random

# l = 10 # int(input("len = "))
# list1 = [random.randint(0, 10) for i in range(l)]
# print(list1)
#
# for i in range(len(list1)-1):
#     for j in range(len(list1)-1-i):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
#
# print(list1)

# row = 4
# col = 4
#
# list2 = [[random.randint(1,9) for j in range(col)] for i in range(row)]
# #print(list2)
# for i in range(row):
#     for j in range(col):
#         print(list2[i][j], end=' ')
#     print()
#
# print()
# sMax = sum(list2[0])
# imax = 0
# for i in range(row):
#     s = sum(list2[i])
#     if s > sMax:
#         sMax = s
#         imax = i
#
# print(imax)
# print(list2[imax])


marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
for l in marks:
    l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])

for student in marks:
    print(student)

lenMax = 0
for student in marks:
    l = len(student)
    if l > lenMax:
        lenMax = l
        studMaxCountMarks = student
print("================================================")
print(studMaxCountMarks)

maxMark = 0
for student in marks:
    markSum = 0
    for i in range(1, len(student)):
        markSum += student[i]
    if markSum > maxMark:
        maxMark = markSum
        studMaxMark = student
print(studMaxMark)


avgMark = 0
for student in marks:
    markSum = 0
    for i in range(1, len(student)):
        markSum += student[i]
    avg = markSum / (len(student)-1)
    if avg > avgMark:
        avgMark = avg
        studAvgMark = student
print(studAvgMark)




# maxElem = list2[0][0]
# for i in range(row):
#     for j in range(col):
#         if list2[i][j] > maxElem:
#             maxElem = list2[i][j]
#
# print(maxElem)

# for list_ in list2:
#     for elem in list_:
#         print(elem, end=' ')
#     print()