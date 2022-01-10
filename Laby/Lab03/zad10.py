
# wyświetli wszystkie liczby mniejsze od 100 i większe od 1 które przy dzieleniu
# przez 5 dają reszczę 1 i przy dzieleniu przez 7 dają resztę 3

n = 1

while n < 100:
    if n % 5 == 1 and n % 7 == 3:
        print(n)
    n += 1

