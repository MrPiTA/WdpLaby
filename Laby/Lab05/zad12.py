
lista = [2,4,7,4,43]

szukana = 4

# wyszukiwanie liniowe

for item in lista:
    if item == szukana:
        print("TAK")
        break

# wyszukiwanie binarne

sorted_lista = sorted(lista)

low = 0
high = len(lista) - 1

while high >= low:
    mid = (low + high) // 2
    if sorted_lista[mid] == szukana:
        print("TAK")
        break
    elif sorted_lista[mid] < szukana:
        low = mid + 1
    else:
        high = mid - 1
