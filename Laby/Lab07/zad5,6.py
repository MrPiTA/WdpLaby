
import random

def linear_comparision(lista,n):
    """zad 5"""
    greater = 0
    equal = 0
    lower = 0

    for item in lista:
        if item > n:
            greater += 1
        elif item == n:
            equal += 1
        else:
            lower += 1

    return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)


def binary_comparision(lista,n):
    """zad 6"""
    lista = lista.sorted()

    greater = 0
    equal = 0
    lower = 0

    if lista[0] <= n <= lista[len(lista)-1]:
        low = 0
        high = len(lista) - 1
        while low <= high:
            mid = (low + high) // 2
            if lista[mid] == n:
                equal += 1
                e_left = 0
                e_right = 0
                if 0 < mid < (len(lista) - 1):
                    if lista[mid + 1] == n:
                        for i in range(mid + 1, high + 1):
                            if lista[i] == n:
                                # equal += 1
                                e_right += 1
                            else:
                                break
                    if lista[mid - 1] == n:
                        for i in reversed(range(low, mid)):
                            if lista[i] == n:
                                # equal += 1
                                e_left += 1
                            else:
                                break
                greater = ((len(lista)-1) - mid) - e_right
                equal = equal + e_right + e_left
                lower = mid - e_left
                return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)
            elif lista[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
    elif n > lista[len(lista)-1]:
        lower = len(lista)
        return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)
    elif n < lista[0]:
        greater = len(lista)
        return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)


def better_binary_comparision(lista,n):

    """nie dokończyłem ulepszać tej funkcji, zbyt dużo czasu mi to zajeło"""

    lista = lista.sorted()

    greater = 0
    equal = 0
    lower = 0

    if lista[0] <= n <= lista[len(lista)-1]:
        low = 0
        high = len(lista) - 1
        while low <= high:
            mid = (low + high) // 2
            if lista[mid] == n:
                equal += 1
                if 0 < mid < (len(lista) - 1):
                    if lista[mid + 1] == n:

                        low_r = mid + 1
                        high_r = high

                        while low_r < high_r:
                            mid_r = (low_r + high_r) // 2
                            if lista[mid_r] == n:
                                low_r = mid_r + 1
                            elif lista[mid_r] > n:
                                high_r = mid_r - 1
                        if lista[mid_r] != n:
                            mid_r -= 1
                        greater = (len(lista) - 1) - mid_r
                        # return greater
                    else:
                        greater = (len(lista) - 1) - mid
                        # return greater



                    if lista[mid - 1] == n:

                        low_l = low
                        high_l = mid - 1

                        while low_l < high_l:
                            mid_l = (low_l + high_l) // 2
                            if lista[mid_l] == n:
                                high_l = mid_l - 1
                            elif lista[mid_l] < n:
                                low_l = mid_l + 1
                        if lista[high_l] == n:
                            high_l -= 1
                        lower = high_l + 1
                        print(lower)
                        break
                    else:
                        lower = mid
                        print(lower)


                # greater = ((len(lista)-1) - mid) - e_right
                # equal = equal + e_right + e_left
                # lower = mid - e_left
                # return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)
            elif lista[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
    elif n > lista[len(lista)-1]:
        lower = len(lista)
        return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)
    elif n < lista[0]:
        greater = len(lista)
        return print("Większych:", greater, "Równych:", equal, "Mniejszych:", lower)



# lista = [random.randint(1,5) for i in range(5)]

lista = [1,1,1,1,2,2,0,-1,-9,-10,3,3,3,3,3,3,3,7,9,9,9,9]

# print(lista)

# linear_comparision(lista,5)

# binary_comparision(lista, 3)

print(better_binary_comparision(lista,3))

