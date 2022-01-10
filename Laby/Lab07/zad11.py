
from random_list_generator_function import random_list_generator

def MoveElements(arr, k):
    if k <= 1:
        return arr
    else:
        tmp = arr.copy()
        for i in range(0, len(arr)):
            arr[(i+k) % len(arr)] = tmp[i]
    return arr

arr = random_list_generator(5,0,5)
print(arr)

print(MoveElements(arr, 7))
