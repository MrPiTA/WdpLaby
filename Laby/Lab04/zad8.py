
# wypisze wszystkie napisy z listy dłuższe niż 3 znaki

list = input("podaj napisy: ").split(",")

print(list)

for item in list:
    if len(item) > 3:
        print(item)