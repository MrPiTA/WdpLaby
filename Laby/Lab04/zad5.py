
list1 = input("Podaj liczby: ").split(",")
list2 = input("Podaj liczby: ").split(",")


for num in list1[:]:
    num_int = int(num)
    list1.remove(num)
    list1.append(num_int)
print(list1)

for num2 in list2[:]:
    num2_int = int(num2)
    list2.remove(num2)
    list2.append(num2_int)
print(list2)

# rozwiązanie 1

# max_list1 = max(list1)
# max_list2 = max(list2)
#
# if max_list1 > max_list2:
#     print(max_list1)
# else:
#     print(max_list2)

# rozwiązanie 2

max_list1 = -1000000000000

for cyfra1 in list1:
    if cyfra1 >= max_list1:
        max_list1 = cyfra1

max_list2 = -1000000000000

for cyfra2 in list2:
    if cyfra2 >= max_list2:
        max_list2 = cyfra2

if max_list1 > max_list2:
    print("Największa wartość z tych list to:", max_list1)
else:
    print("Największa wartość z tych list to:", max_list2)
