
# wypisze TAK, jeśli dwie listy mają wspólny element,albo NIE

# 1 sposób

list1 = [123, "A", "a", "abc"]

list2 = [1232, "abc"]

# flag = 0
#
# for item in list2:
#     if item in list1:
#         flag = 1
#
# if flag == 1:
#     print("TAK")
# else:
#     print("NIE")

# 2 sposób - zbiory

set1 = set(list1)
set2 = set(list2)

# też można  zrobić to co u góry, ale dla tych zbiorów
# one są zoptymizowane pod to

if set1.intersection(set2) != set():
    print("TAK")
else:
    print("NIE")


