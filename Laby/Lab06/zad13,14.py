
import random


def linear_existence_checker(lista, item):
    """zad 13"""
    for i in lista:
        if i == item:
            return "Znaleziono"
    return "Nie znaleziono"

def binary_existence_checker(lista, item):
    # sortuje listę
    lista.sort()
    #
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == lista[mid]:
            return "Znaleziono"
        elif item > lista[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return "Nie znaleziono"





lista = [random.randint(0, 10) for i in range(5)]

print(lista)
print(binary_existence_checker(lista,2))

# print(linear_existence_checker(lista, 5))

