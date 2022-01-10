

def place_changer(lista, index1, index2):
    # tworzymy kopię listy
    lista_copy = lista[:]
    # podmieniamy w kopii wartości
    lista_copy[index1] = lista[index2]
    lista_copy[index2] = lista[index1]
    # zwracamy listę z zmienionymi wartoścami
    return lista_copy


lista = [1,2,3,4,5]

print(place_changer(lista, 1, -2))