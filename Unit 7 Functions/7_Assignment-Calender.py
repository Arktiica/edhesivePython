def leap_year(y):
    if (y % 4 == 0):
        return 1
    else:
        return 0
def number_of_days(m, y):
    feb = leap_year(y)
    if (m == 1): # January
        return 31
    elif (m == 2): # February
        return feb + 28
    elif (m == 3): # March
        return 31
    elif (m == 4): # April
        return 30
    elif (m == 5): # May
        return 31
    elif (m == 6): # June
        return 30
    elif (m == 7): # July
        return 31
    elif (m == 8): # August
        return 31
    elif (m == 9): # September
        return 30
    elif (m == 10): # October
        return 31
    elif (m == 11): # November
        return 30
    elif (m == 12): # December
        return 31

def days(d, m):
    if (m == 1):
        return 0 + d
    elif (m == 2):
        return 31 + d
    elif (m == 3):
        return 59 + d
    elif (m == 4):
        return 90 + d
    elif (m == 5):
        return 120 + d
    elif (m == 6):
        return 151 + d
    elif (m == 7):
        return 181 + d
    elif (m == 8):
        return 212 + d
    elif (m == 9):
        return 243 + d
    elif (m == 10):
        return 273 + d
    elif (m == 11):
        return 304 + d
    elif (m == 12):
        return 334 + d

def days_left(d, m, y):
    x = days(d, m)
    if (x <= 60):
        return 365 - x + leap_year(y)
    else:
        return 365 - x

print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
menu = int(input("Menu:\n1) Calculate the number of days in the given month.\n2) Calculate the number of days left in the given year.\n"))

numDays = str(number_of_days(month, year))
daysLeft = days_left(day, month, year)

if (menu == 1):
    print(numDays)
elif (menu == 2):
    print(daysLeft)
