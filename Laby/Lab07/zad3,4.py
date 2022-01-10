
import random

# zad 3

def linear_last_indeks_searcher(lista, n):
    """zad 3"""
    indeks = "Not found"
    for i in range(len(lista)):
        if lista[i] == n:
            indeks = i
    return indeks

# zad 4

def binary_last_indeks_searcher(lista, n):
    """zad 4"""
    indeks = "Not found"
    lista.sort()
    # print(lista)
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == n:
            if mid < len(lista) - 1:
                if lista[mid+1] == n:
                    for i in range(mid+1,high+1):
                        if lista[i] == n:
                            indeks = i
                        else:
                            break
                    return indeks
            indeks = mid
            return indeks
        elif lista[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return indeks




lista = [random.randint(1,10) for i in range(6)]

print(lista)
print(linear_last_indeks_searcher(lista, 3))
print(binary_last_indeks_searcher(lista, 3))