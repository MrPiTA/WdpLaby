
# do 66

number = input("number: ")

number_int = int(number)

first = int(number_int % 10)
second = int((number_int-first)/10)


ones = ["one", "two", "three", "four", "five", "six"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty"]

print(tens[second-1]+"-"+ones[first-1])