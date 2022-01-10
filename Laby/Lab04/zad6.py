
list = input("liczby: ").split(",")

for num in list[:]:
    num_float = float(num)
    list.remove(num)
    list.append(num_float)

print(list)

# rozwiązanie 1

# print("Wartość:",min(list), "Index:", list.index(min(list)))

# rozwiązanie 2

indeks = []
list_min = list[0]
d = 0

for n in range(0, len(list)):
    if list[n] == list_min:
        indeks.append(d)
        continue
    if list[n] < list_min:
        d -= 1
        list_min = list[n]
        indeks.append(d)
        continue
    indeks.append(1)

 # najmniejsza wartość 1
# print("Najmniejsza wartość:", list_min, end=", ")
# print(indeks)


# znalezienie index(u)/(ów)

min_indek = 0
indeksy = []

print("indeks: ", end="")

for indek in indeks:
    if indek == d:
        print(min_indek,end=",")
        indeksy.append(min_indek)
    min_indek += 1


print("Najmniejsza wartość:", list[indeksy[0]])


# najmniejsza wartość 2




# popped = indeks[-1]
# max_indeks = len(indeks)-1
#
# for indek in indeks[:]:
#     popped = indeks.pop()
#     if popped == 1:
#         break
#     max_indeks -= 1
#
# print("jej indeks:", max_indeks)






# copy

# for num in list:
#     if num <= list_min:
#         list_min = num
#         indeks.append(1)
#         continue
#     indeks.append(0)
#
# print("Najmniejsza wartość:", list_min, end=", ")
# # print(indeks)
#
# popped = indeks[-1]
# max_indeks = len(indeks)-1
#
# for indek in indeks[:]:
#     popped = indeks.pop()
#     if popped == 1:
#         break
#     max_indeks -= 1
#
# print("jej indeks:", max_indeks)



