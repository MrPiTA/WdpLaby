
# wypisuje na ekran wszystkie liczby, których cyfry są ułożone w kolejności rosnącej

# 123, 234, 467


for x in range(100,1000):
    j = x % 10
    d = ((x % 100) - j) / 10
    s = (x % 1000 - x % 100) / 100
    if s < d < j:
        print(x)