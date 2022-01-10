
slowo = input("slowo: ")

slowo_list = []

for litera in slowo:
    slowo_list.append(litera)

print(slowo_list)

# rozwiązanie

wzorzec = ["a","b"]

flag = 0

for l in range(len(slowo_list)):
    if slowo_list[l] == wzorzec[0]:
        if slowo_list[l+1] == wzorzec[1]:
            print("TAK")
            flag = 1
            break

if flag == 0:
    print("NIE")



# rozwiązanie 2 xd

# slowo = "alan"
# wzorzec = "ala"
#
# if wzorzec in slowo:
#     print("TAK")
