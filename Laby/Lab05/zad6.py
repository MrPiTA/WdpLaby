
lista = [
    [1,2,4,6],
    [2,3,4,5],
    [12,3,4,5]
]

# rozwiązanie

for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j] *= 3

print(lista)