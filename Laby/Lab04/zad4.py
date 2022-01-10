
liczby = input("liczby: ")

list = liczby.split(",")

for item in list[:]: # wow, rozwiązanie tego problemu jest z opisu for z pycharm
    item_int = int(item)
    list.remove(item)
    list.append(item_int)
print(list)

iloczyn = 1
for liczba in list:
    iloczyn *= liczba

print(iloczyn)