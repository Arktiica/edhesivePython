def divis(a):
    for r in range(len(a)):
        for c in range (len(a[0])):
            if (a[r][c] % 3 == 0):
                a[r][c] = a[r][c]
            else:
                a[r][c] = 0

a = [[34, 38, 50, 44, 39], 
     [42, 36, 40, 43, 44], 
     [24, 31, 46, 40, 45], 
     [43, 47, 35, 31, 26], 
     [37, 28, 20, 36, 50]]

divis(a)
for r in range(len(a)):
    for c in range(len(a[r])):
        print((a[r][c]), end = " ")
    print(" ")
