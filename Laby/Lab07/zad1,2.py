
import random

def random_nums_in_list(n):

    """zad 1"""

    lista = [random.randint(0,100) for i in range(n)]

    return lista

def sorted_random_nums_in_list(n):

    """zad 2"""

    lista = []
    num1 = random.randint(1, 50)
    lista.append(num1)
    low = 51
    high = 100
    for i in range(n-1):
        num = random.randint(low, high)
        lista.append(num)
        low += 50
        high += 50

    return lista




# print(random_nums_in_list(5))
print(sorted_random_nums_in_list(5))