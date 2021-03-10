from random import randint

def buildArray(a, b):
    for i in range(int(b)):
        a.append(randint(10,99))

def sumArray(a):
    sum = 0
    for i in (a):
        sum = sum + i
    return(sum)

x = []
n = input("Number of values to add to the array: ")
buildArray(x, n)
print(x)
print("Total " + str(sumArray(x)))
