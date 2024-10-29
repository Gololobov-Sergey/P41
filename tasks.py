def bubbleSort(list_, method):
    for i in range(len(list_)-1):
        for j in range(len(list_)-1-i):
            if method(list_[j], list_[j+1]):
                list_[j], list_[j+1] = list_[j+1], list_[j]

def sort_date(list1, list2):
    return list1[0] > list2[0]

def sort_name(list1, list2):
    return list1[1] > list2[1]
def sort_pri(list1, list2):
    return list1[2] > list2[2]

tasks = []

def add_task():

    print("New task")
    tasks.append([input("Date: "), input("Name: "), int(input("Priority: "))])
    save()

def edit_task():
    print_task()
    choice = int(input("Select number task: "))
    param = int(input("Select param, 1-Date, 2-Name, 3-Priority : "))
    if param == 1:
        tasks[choice-1][0] = input("New date: ")
    elif param == 2:
        tasks[choice - 1][1] = input("New name: ")
    elif param == 3:
        tasks[choice - 1][2] = int(input("New priority: "))
    save()

def del_task():
    print_task()
    choice = int(input("Select number task: "))
    tasks.remove(tasks[choice - 1])
    save()

def print_task():
    for i in range(len(tasks)):
        print(i + 1, tasks[i][0], tasks[i][1], tasks[i][2])
    print()

def sort_task():
    param = int(input("Select param, 1-Date, 2-Name, 3-Priority : "))
    if param == 1:
        bubbleSort(tasks, sort_date)
    elif param == 2:
        bubbleSort(tasks, sort_name)
    elif param == 3:
        bubbleSort(tasks, sort_pri)

def save():
    f = open("tasks.txt", "w")
    for i in range(len(tasks)):
        f.write(f"{tasks[i][0]}, {tasks[i][1]}, {tasks[i][2]}, \n")
    f.close()

def load():
    f = open("tasks.txt", "r")
    t = f.readlines()
    for i in t:
        i = i.replace('\n', '')
        ts = i.split(', ')
        tasks.append([ts[0], ts[1], int(ts[2])])
    f.close()

def menu():
    while True:
        print("1. Add task")
        print("2. Edit task")
        print("3. Del task")
        print("4. Sort task")
        print("5. Print task")
        choice = int(input("Enter number : "))
        if choice == 1:
            add_task()
        elif choice == 2:
            edit_task()
        elif choice == 3:
            del_task()
        elif choice == 4:
            sort_task()
        elif choice == 5:
            print_task()

load()
menu()