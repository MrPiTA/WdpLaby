
cyfry = input("cyfry: ")

list = []

for cyfra in cyfry:
    cyfra_int = int(cyfra)
    list.append(cyfra_int)

print(list)

# rozwiązanie 1

# print(sum(list))

# rozwiązanie 2

suma = 0
for cyfra in list:
    suma += cyfra
print(suma)

