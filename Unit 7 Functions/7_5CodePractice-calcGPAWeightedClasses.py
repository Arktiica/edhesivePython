def GPAcalc(g, w):
    if g.lower() == 'a':
        return 4 + w
    elif g.lower() == 'b':
        return 3 + w
    elif g.lower() == 'c':
        return 2 + w
    elif g.lower() == 'd':
        return 1 + w
    elif g.lower() == 'f':
        return 0 + w
    else:
        return "Invalid"

def weighGPA(x, y):
    z = y / x - 0.5
    return  format(float(z))

initMsg = int(input("How many classes are you taking? "))

someArray = []

totalGPA = 0
for i in range (initMsg):
    msg = input("\nEnter your letter grade: ")
    msg2 = int(input("Is it weighted? (0 = no, 1 = yes) "))
    gpa = GPAcalc(msg, msg2)
    print("Your GPA score is: " + str(gpa))
    someArray.append(gpa)

print(f"\nYour weighted GPA is {format(float(totalGPA / initMsg))}")
