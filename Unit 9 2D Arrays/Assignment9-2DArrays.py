def printArray(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end = " ")
        print(" ")

def flipHorizontal(a):
    temp = []
    for i in range(0, len(a)):
        pos = []
        for j in range (0, len(a[0])):
            pos.append(a[i][len(a[0]) - j - 1])
        temp.append(pos)
    printArray(temp)


def flipVertical(a):
    rev = a[::-1]
    printArray(rev)

arr = []
arr.append([0, 2, 0, 0, 0])
arr.append([0, 2, 0, 0, 0])
arr.append([0, 2, 2, 0, 0])
arr.append([0, 2, 0, 2, 0])
arr.append([0, 2, 0, 0, 2])

printArray(arr)
print()
flipHorizontal(arr)
print()
arr = [[0 , 2 , 0 , 0 , 0] , [0 , 2 , 0 , 0 , 0] , [0 , 2 , 2 , 0 , 0] , [0 , 2 , 0 , 2 , 0] , [0 , 2 , 0 , 0 , 2]]
flipVertical(arr)

# Output:
#   Normal Order
#       0 2 0 0 0
#       0 2 0 0 0
#       0 2 2 0 0
#       0 2 0 2 0
#       0 2 0 0 2
#
#   Horizontally Flipped Order
#       0 0 0 2 0
#       0 0 0 2 0
#       0 0 2 2 0
#       0 2 0 2 0
#       2 0 0 2 0
#
#   Vertically Flipped Order
#       0 2 0 0 2
#       0 2 0 2 0
#       0 2 2 0 0
#       0 2 0 0 0
#       0 2 0 0 0
