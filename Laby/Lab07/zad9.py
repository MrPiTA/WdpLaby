
from random_list_generator_function import random_list_generator


def find_biggest(lista):
    if lista:
        biggest = lista[0]
        max_index = 0
        for i in range(1,len(lista)):
            if lista[i] > biggest:
                biggest = lista[i]
                max_index = i
        return max_index

def from_biggest_selection_sort(lista):
    lista = lista[:] # działamy na kopii
    new_lista = []
    for i in range(len(lista)):
        biggest = find_biggest(lista)
        new_lista.append(lista.pop(biggest))
    return new_lista


# dla siebie, to samo ale od najmniejszej

def find_smallest(lista):
    smallest = lista[0]
    smallest_index = 0
    for i in range(1,len(lista)):
        if lista[i] < smallest:
            smallest = lista[i]
            smallest_index = i
    return smallest_index


def from_smallest_selection_sort(lista):
    lista = lista[:]
    new_lista = []
    for i in range(len(lista)):
        smallest = find_smallest(lista)
        new_lista.append(lista.pop(smallest))
    return new_lista


lista = random_list_generator(5,-5,5)

print(lista)
# print(find_biggest(lista))
# print(from_biggest_selection_sort(lista))
# print(lista)
print(from_smallest_selection_sort(lista))
