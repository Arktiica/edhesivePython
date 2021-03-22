from random import randint

numbers = []

for r in range (4):
    numbers.append([])

for r in range (len(numbers)):
    for c in range (5):
        numbers[r].append(randint(-30,30))

for r in range (len(numbers)):
    for c in range (len(numbers[0])):
         print((numbers[r][c]), end = " ")
    print("")
