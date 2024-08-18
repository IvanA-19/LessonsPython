# Вложенные списки
a = [[0, 1, 2], [3, 4, 5], [4, 5, 6]]
print(a)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(i, j, end=".")
        print(a[j][i])


# Словари
# Набор данных, которые хранятся в паре ключ-значение
# dict()

d = {
    "name": "Вася",
    "age": 19,
    "result": False
}

print(d)
d["clever"] = True
print(d)

# Перебор словаря
for key, value in zip(d.keys(), d.values()):
    print(key, d[key])

# keys() - возвращает массив ключей
# values() - возвращает массив значений

# Словарь списков
"""
d_l = {"Name": [], "age": [], "ЗП": []}
val = ""
while True:
    for i in range(3):
        val = input()
        d_l[d_l.keys()[i]].append(val)
    if val == "0":
        break
        
write_data_to_db(d_l)
"""