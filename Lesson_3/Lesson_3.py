# Списки
# Переменная типа list
# Список позволяет хранить в одной переменной много значений

# Явное задание списка
a = [1, 2, 5, 90, 12, 6]

print(a)

# Обращение к элементам происходит по индексу
# Каждый элемент имеет свой номер
# Индексация начинается с 0
print(a[0])
print(a[3])

# Перебор списка
# 1. По индексу
# 2. По коллекции

# Для получения длины списка используется len()
for i in range(len(a)):
    print(a[i])

print()
for element in a:
    print(element)

print()
# Смешанный перебор
for i, element in enumerate(a):
    print(i, element)

# Методы списков
# Добавление элементов
# Производится с помощью append()

print()
print(a)
a.append(8)
print(a)

# Добавление не в конец insert()
a.insert(1, 321)
print(a)

# count() - возвращает сколько раз встречается элемент
print(a.count(6))
a.append(6)
print(a.count(6))

# index() возвращает индекс элемента в списке, если он есть
print(a.index(6))

# Удаление
# pop() - удаляет элемент по индексу и его возвращает.
# Если нет аргументов - удаляет последний элемент

print(a)
a.pop()
print(a)
print(a.pop(1))
print(a)

# remove() - удаляет элемент по значению

print(a)
a.remove(90)
print(a)

# sort() / sorted() - сортирует список по возрастанию /
# возвращает отсортированный по возрастанию список

print()
print(a)
print(sorted(a))
print(a)
a.sort()
print(a)

# reverse() - переписывает список с конца в начало

a.reverse()
print(a)


# Срезы
# Нижний включительно, верхний не включительно
print(a[:4]) # [12, 8, 6, 5]
print(a[2:]) # [6, 5, 2, 1]

print(a[2:4]) # [6, 5]

print(a[1::2]) # [8, 5, 1]

# Переворачивает список
print(a[::-1])

# Кортежи - неизменяемые списки
b = (2, 3, 5, 6, 9)

# Списки поддерживают min() и max()
print(min(a), max(a))

# Задача 1. Вывести на экран таблицу истинности для основных операций алгебры логики
# Конъюнкция (и)
"""
x   y   f = x and y
0   0       0
0   1       0
1   0       0
1   1       1
"""
print("x\ty\tf = x and y")
for x in range(2):
    for y in range(2):
        print(f"{x}\t{y}\t\t{x and y}")

# Дизъюнкция (или)
print("x\ty\tf = x or y")
for x in range(2):
    for y in range(2):
        print(f"{x}\t{y}\t\t{x or y}")

# Импликация (A -> B)
print("x\ty\tf = x -> y")
for x in range(2):
    for y in range(2):
        print(f"{x}\t{y}\t\t{x <= y}")

# Генераторы списков
# Классический способ заполнения списка
b = []

for i in range(11):
    b.append(i)

print(b)

c = [i if i % 2 == 0 else 0 for i in range(11)]
print(c)
print(list(set(c)))

# set - множество
# множество содержит только уникальные значения

# Задача 2. Имеется список целых чисел от -100, 100.
# Найти в списке под каким номером находится
# Данное число
# Список отсортирован по возрастанию

arr = [e for e in range(-100, 101)]
# arr = list(range(-100, 101))

num = int(input("Введите число от -100 до 100: "))
# Бинарный поиск

low = 0
high = len(arr) - 1

step_count = 0
while low <= high:
    mid = (high + low) // 2
    guess = arr[mid]
    if guess == num:
        print(mid)
        break
    if guess > num:
        high = mid - 1
    if guess < num:
        low = mid + 1
    step_count += 1

print(arr.index(num))
print(step_count)

