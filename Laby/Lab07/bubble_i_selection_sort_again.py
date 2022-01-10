
from random_list_generator_function import random_list_generator


def FindMinIndex(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def SelectionSort(arr):
    arr = arr[:]
    new_arr = []
    for i in range(len(arr)):
        smallestIndex = FindMinIndex(arr)
        new_arr.append(arr.pop(smallestIndex))
    return new_arr


def BubbleSort(arr):
    """zoptymalizowana wersja - liczy swapy"""
    arr = arr[:]
    swap_counter = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_counter += 1
        if swap_counter == 0:
            return arr
        swap_counter = 0
    return arr

arr = random_list_generator(5,0,5)
print(arr)
print(SelectionSort(arr))
print(BubbleSort(arr))
