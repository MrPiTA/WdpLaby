
import random

def print2D(tablica):
    for i in range(len(tablica)):
        print(tablica[i])

n = 3
lista = [[random.randint(0,9) for i in range(n)] for j in range(n)]

print2D(lista)

# rozwiązanie

# przechowuje sum list
suma = []

# oblicza sumy list

suma_listy = 0

for i in range(len(lista)):
    suma_listy = sum(lista[i])
    suma.append(suma_listy)

# print(suma)

# wypisuje listę o największej sumie

print("Lista o największej sumie:")

maks = max(suma)
for i in range(len(suma)):
    if maks == suma[i]:
        print(lista[i])

# wypisuje listę o najmniejszej sumie

print("Lista o najmniejszej sumie:")

minimum = min(suma)
for i in range(len(suma)):
    if minimum == suma[i]:
        print(lista[i])






