
lista = [1,3,5,7,9,10]

sub_list = [2,4,6,8]

# rozwiązanie

lista[-1] = sub_list[0]
lista = lista + sub_list[1:]

print(lista)