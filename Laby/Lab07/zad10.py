
from random_list_generator_function import random_list_generator

def BubbleSort(lista):
    """zoptymalizowana wersja - liczy swapy"""
    lista = lista[:]
    swap_counter = 0
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista = place_changer(lista, j, j+1)
                swap_counter += 1
        if swap_counter == 0:
            return lista
        swap_counter = 0
    return lista



def place_changer(lista, index1, index2):
    # tworzymy kopię listy
    lista_copy = lista[:]
    # podmieniamy w kopii wartości
    lista_copy[index1] = lista[index2]
    lista_copy[index2] = lista[index1]
    # zwracamy listę z zmienionymi wartoścami
    return lista_copy


# lista = [1,5,3,6,4,7]
# SortedList = [1, 3, 4, 5, 6, 7]
lista2 = random_list_generator(5,0,100)
empty_list = []
# print(BubbleSort(lista))
# print(BubbleSort(SortedList))
# print(lista2)
print(BubbleSort(lista2))
# print(BubbleSort(empty_list))