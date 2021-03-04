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

msg = input("Enter your letter grade:")
msg2 = int(input("Is it weighted? (0 = no, 1 = yes) "))
gpa = GPAcalc(msg, msg2)
print("Your GPA score is: " + str(gpa))
