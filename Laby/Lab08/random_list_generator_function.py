import random

def random_list_generator(length, min, max):
    result = [random.randint(min,max) for i in range(length)]
    return result