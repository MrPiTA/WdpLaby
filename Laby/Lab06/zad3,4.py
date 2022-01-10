
import random

def sum_elementow(lista):
    """zad 3"""
    if lista:
        suma = 0
        for item in lista:
            suma += item
        return suma
    else:
        return "given list is empty"

def iloczyn_elementow(lista):
    """zad 4"""
    if lista:
        iloczyn = 1
        for item in lista:
            iloczyn *= item
        return iloczyn
    else:
        return "given list is empty"



lista = [random.randint(0,5) for i in range(5)]

empty = []

print(lista)

print(sum_elementow(lista))

print(iloczyn_elementow(lista))

print(sum_elementow(empty))
print(iloczyn_elementow(empty))