a = [[34, 38, 50, 44, 39], 
     [42, 36, 40, 43, 44], 
     [24, 31, 46, 40, 45], 
     [43, 47, 35, 31, 26],
     [37, 28, 20, 36, 50]]
     
total = 0
for r in range (len(a)):
    for c in range(len(a[0])):
        total += a[r][c]
        avg = (total / a[r][c]) * 2

print("Sum of all values: " + str(total))
print("")
print("Average of all values: " + str(avg))
