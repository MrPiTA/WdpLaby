
import random

list = [random.randint(1,20) for i in range(5)]

print(list)

sorted_list = sorted(list)

for i in range(len(sorted_list)-1):
    if sorted_list[len(sorted_list)-2-i] < sorted_list[len(sorted_list)-1]:
        print(sorted_list[len(sorted_list)-2-i])
        break
