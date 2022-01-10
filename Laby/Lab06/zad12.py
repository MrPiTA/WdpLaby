
def sort_checker(list):
    for i in range(len(list)-1):
        if list[i] > list[i + 1]:
            return "NIE"
    return "TAK"


my_list = [1,3,2,4,5,6,7,5,3,2,3,5,6,7]
my_list2 = sorted(my_list)

print(my_list)
print(my_list2)

print(sort_checker(my_list))
print(sort_checker(my_list2))