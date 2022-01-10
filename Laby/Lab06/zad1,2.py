
# zad 1

def is_greater(a,b):
    """chooses grater number from two numbers"""
    if a == b:
        return a
    elif a > b:
        return a
    else:
        return b


print(is_greater(8,10))


# zad 2

a = 7
b = 3
c = 7


if is_greater(a,b) >= is_greater(b,c) and is_greater(a,b) >= is_greater(a,c):
    print(is_greater(a,b))
elif is_greater(b,c) > is_greater(a,b) and is_greater(b,c) > is_greater(a,c):
    print(is_greater(b,c))
else:
    print(is_greater(a,c))
