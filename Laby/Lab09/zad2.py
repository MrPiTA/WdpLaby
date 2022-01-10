
def IsPermutation(arr1, arr2):
    if len(arr1) == len(arr2):
        if arr1 == arr2:
            return False
        elif arr1 and arr2:
            return CheckElements(arr1,arr2)
        else:
            return False
    else:
        return False

def CheckElements(arr1, arr2):
    for item in arr1:
        if item not in arr2:
            return False
    return True



L1 = [1, 2, 3, 4, 5]
L2 = [5, 4, 3, 2, 1]
empty = []
L3 = [5, 4, 3, 2, 10]
L4 = [1,2,3,4,5,6,7,8,9,0]

print(IsPermutation(L1, L2))
print(IsPermutation(L1, empty))
print(IsPermutation(L1, L3))
print(IsPermutation(L1, L4))





