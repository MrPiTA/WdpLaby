

def print2D(tablica):
    for i in range(len(tablica)):
        print(tablica[i])

macierz = [
    [7, 2, 8, -1],
    [1, 3, 2, 0],
    [-5, 9, 5, -7]
]

print2D(macierz)

print("\r")

# macietrz transponowana

transponowana = [ [" " for i in range(len(macierz))] for j in range(len(macierz[0]))]

# print2D(transponowana)

for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        transponowana[j][i] = macierz[i][j]

print2D(transponowana)