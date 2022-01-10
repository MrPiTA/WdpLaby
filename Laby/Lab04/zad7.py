
# znajduje drugą największą wartość w liście i jej indeks
# nie może być duplikatów w liście


list = input("liczby: ").split(",")

for num in list[:]:
    num_float = float(num)
    list.remove(num)
    list.append(num_float)

print(list)

# rozwiązanie

# a = list[:]
#
# a.remove(max(a))
#
# second_max = max(a)
#
# indeks = list.index(second_max)
#
# print("Druga największa wartość:",second_max)
# print("Jej indeks: ", indeks)

# rozwiązanie 2


a = list[:]

indeks = []
list_max = list[0]

for num in list:
    if num >= list_max:
        list_max = num
        indeks.append(1)
        continue
    indeks.append(0)

# print("Największa wartość:", list_max)
print(indeks)

popped = indeks[-1]
max_indeks = len(indeks)-1

flag = 0

for indek in indeks[:]:
    popped = indeks.pop()
    if popped == 1:
        if flag == 0:
            flag += 1
            max_indeks -= 1
            continue
        break
    max_indeks -= 1

if len(list) > 1:
    print("druga największa wartość:", list[max_indeks])
    print("jej indeks:", max_indeks)
else:
    print("lista nie ma drugiej największej wartości")

