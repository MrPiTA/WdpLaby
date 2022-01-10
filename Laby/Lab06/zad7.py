

def bez_powtorzen(lista):
    spacje = 0
    k = 0
    for i in range(len(lista)):
        if k < len(lista):
            k += 1
        if lista[i] == [" "]:
            continue
        for j in range(k,len(lista)):
            if lista[j] == " ":
                continue
            if lista[i] == lista[j]:
                lista[j] = " "
                spacje += 1

    for s in range(spacje):
        lista.remove(" ")

    return lista

def bez_powtorzen2(lista):
    res = []
    for item in lista:
        if item not in res:
            res.append(item)
    return res

def bez_powtorzen3(lista):
    """nie zawsze w odpowiedniej kolejności będzie wyświetlać"""
    lista = list(set(lista))
    return lista



lista = [1,2,3,2,2,4,5,3,1,4,3,5,2,3,4,5,6,7,3,2,4,6,7,3,4]

print(bez_powtorzen(lista))

print(bez_powtorzen2(lista))

print(bez_powtorzen3(lista))