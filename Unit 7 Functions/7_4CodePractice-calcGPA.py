def GPAcalc(g):
    if g.lower() == 'a':
        return 4
    elif g.lower() == 'b':
        return 3
    elif g.lower() == 'c':
        return 2
    elif g.lower() == 'd':
        return 1
    elif g.lower() == 'f':
        return 0
    else:
        return "Invalid"

m = input("Enter your letter grade:")
gpa = GPAcalc(m)
print("Your GPA score is: " + str(gpa))
