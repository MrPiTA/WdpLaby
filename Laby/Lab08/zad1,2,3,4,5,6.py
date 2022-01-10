
from random_list_generator_function import random_list_generator

def factorial(n):
    """zad 1"""
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibb(n):
    """zad 2"""
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)


def sumaEpsilon(n):
    """zad 3"""
    if n == 1:
        return 1
    else:
        return (1/n) + sumaEpsilon(n-1)


def potegowanieBezPotegowaniaMnozenia(n):
    """zad 4"""
    k = n
    def suma(n):
        if n < 0:
            return "error"
        elif n <= 1:
            return k
        else:
            return k + suma(n-1)
    return suma(n)


def SumaParzystychOd1DoN(n):
    """zad 5"""
    def DodajParzyste(n):
        if n < 0:
            return "error"
        elif n == 0:
            return 0
        else:
            return n + DodajParzyste(n-2)

    if n % 2 == 0:
        return DodajParzyste(n)
    else:
        return DodajParzyste(n-1)


def RecursiveBinarySearch(arr, item):
    """zad 6 - słaby sposób"""
    arr.sort()
    low = 0
    high = len(arr) - 1
    def RecursiveSearch(low,high):
        if low <= high:
            mid = (low + high) // 2
            if arr[mid] == item:
                return True
            elif arr[mid] > item:
                high = mid - 1
                return RecursiveSearch(low,high)
            else:
                low = mid + 1
                return RecursiveSearch(low,high)
        else:
            return False
    return RecursiveSearch(low,high)


def BetterRecursiveBinarySearch(arr, low, high, x):
    """zad 6 - lepszy sposób"""
    arr = sorted(arr)
    # base case
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BetterRecursiveBinarySearch(arr, low, mid - 1, x)
        else:
            return BetterRecursiveBinarySearch(arr, mid + 1, high, x)
    else:
        return -1


def RecursionlinearSearch(arr, x, start=0):
    """tak dla siebie to napisałem"""
    if start <= len(arr)-1:
        if arr[start] == x:
            return start
        else:
            return RecursionlinearSearch(arr, x, start+1)
    else:
        return -1


arr = random_list_generator(5, 0, 10)
print(arr)
print(RecursionlinearSearch(arr, 2))

# print(sorted(arr))
# result = BetterRecursiveBinarySearch(arr, 0, len(arr)-1, 2)
# if result != -1:
#     print("Element is present at index:", result)
# else:
#     print("Element is not present")



# testy do Recursi......
# arr1 = [6, 3, 0, 8, 7]
# arr2 = [6, 3, 2, 8, 7]
# print(RecursiveBinarySearch(arr, 2))

# print(factorial(3))

# print(fibb(8))

# print(sumaEpsilon(5))

# print(potegowanieBezPotegowaniaMnozenia(4))

# print(SumaParzystychOd1DoN(-6))