

def print2D(lista):
    for i in range(len(lista)):
        print(lista[i])
    return 0

def reverse_print2D(lista):
    for i in range(len(lista)):
        rev = reversed(lista[i])
        print(list(rev))
    return 0


n = int(input("n: "))
m = int(input("m: "))

tablica = [[j for j in range(m)] for i in range(n)]

# print(tablica)

# print2D(tablica)

reverse_print2D(tablica)
