def printIt(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end = " ")
        print(" ")
    print(" ")
    
    for r in range(len(a)):
        x = a[r][r]
        for c in range(len(a[0])):
            a[r][c] = x
            
    for r in range(len(a)):
        for c in range (len(a[0])):
            print(a[r][c], end = " ")
        print(" ")
    

N = []
N.append([1, 2, 3, 4, 5])
N.append([1, 2, 3, 4, 5])
N.append([1, 2, 3, 4, 5])
N.append([1, 2, 3, 4, 5])

printIt(N)
