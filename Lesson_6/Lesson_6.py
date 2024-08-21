# Работа со строками и файлами

# Строковые методы

s = "Hello, world! Have a nice day! Hello"
print(len(s))

# split() разделяет строку на список подстрок по заданному символу
# или строке (по умолчанию по пробелу)
print(s.split())

# upper() - приводит строку к верхнему регистру

# lower() - приводит строку к нижнему регистру


print(s.upper(), s.lower())

# index() возвращает индекс под которым встречается первое вхождение
# подстроки в текущую строку
print(s.index("Ha"))

# count() возвращает количество вхождений подстроки в текущую строку
print(s.count("H"))

# replace() меняет подстроку в текущей строке на другую.
# по умолчанию заменяет все вхождения данной подстроки
print(s.replace("Hello", "Hi", 1))

# join() собирает строку из итерируемого объекта по заданному
# разделителю

words = ['Hello,', 'world!', 'Have', 'a', 'nice', 'day!']
print(", ".join(word for word in words))

# Работа с файлами
# Чтение данных из файла
print()
with open("hello.txt", "r") as r_file:
    print(r_file.readline())
    for s in r_file:
        print(s)

# Запись в файл
with open("hello.txt", "w") as w_file:
    w_file.write("Rain")

# Дан файл task.txt, состоящий из 10^6 символов
# X, Y, Z. Необходимо найти наибольшую длину строки,
# состоящей из Z


with open("24_demo.txt", "r") as file:
    string = file.readline()
    count = 1
    max_count = 1

    # XXXZZXYYXYYYYXXXXXXXXZYX

    for c in range(len(string) - 1):
        if string[c] == string[c + 1] == "X":
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    print(max_count)



