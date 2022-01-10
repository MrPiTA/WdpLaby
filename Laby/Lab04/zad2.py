
samogloski = ["a","e","i","o","u","ó","y","ą","ę"]

napis = input("napis: ")

napis = napis.lower()

lista_napis = []

for znak in napis:
    lista_napis.append(znak)

# print(lista_napis)

liczb_sglosek = 0

for znak in lista_napis:
    if znak in samogloski:
        liczb_sglosek += 1
        print(znak, end=", ")
print("Liczba samogłosek: ", liczb_sglosek)





