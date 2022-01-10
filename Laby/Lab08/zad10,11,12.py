
from random_list_generator_function import random_list_generator

def head(arr):
    popped = arr.pop(0)
    return popped


def tail(arr):
    arr = arr[:]
    head(arr)
    return arr

def IsEmpty(arr):
    if arr:
        return False
    else:
        return True

def rewers(arr):
    if not IsEmpty(arr):
        arr = tail(arr)
        print(arr)
        def swap(arr, i=0):
            if i < len(arr)-1:
                arr.insert(i, arr.pop(-1))
                return swap(arr, i+1)
            else:
                return arr

        return swap(arr)






arr = random_list_generator(5,0,5)
print(rewers(arr))

# print(head(arr))
# print(tail(arr))
# print(arr)
# print(IsEmpty(arr))