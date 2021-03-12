# Check for and adjust month input if necessary
def validateMonth(month):
    if month >= 1 and month <= 12:
        return month
    else:
        return 1

# Check for and adjust day input if necessary
def leapYear(year):         # Determines leap year
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True

def numberOfDays(month, year):    # Returns the number of days: 28, 29, 30, 31
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    elif (month == 2):
        if (leapYear(year) == True):
            return 29
        else:
            return 28
            
def validateDay(month, day, year):
    if day < 1 or day > numberOfDays(month, year):
        return 1
    else:
        return day

# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def printEvents(eventName, eventMonth, eventDay, eventYear):
	months = ['January','February','March','April','May','June','July','August', 'September','October','November','December']
	print("")
	print("******************** List of Events ********************")
	for i in range(len(eventName)):
# 		print(eventName[i])
		print(str(eventName[i]) + "\nDate: " + str(months[eventMonth[i]-1]) + " " + str(eventDay[i]) + ", " + str(eventYear[i]))

# This function is used to prompt, adjust and
# append values to the 4 parallel arrays
def addEvent():
    while (True):
        newName = input("What is the event: ")
        newMonth = int(input("What is the month (number): "))
        newDay = int(input("What is the day: "))
        newYear = int(input("What is the year: "))
        print("")
        
        newMonth = validateMonth(newMonth)
        newDay = validateDay(newMonth, newDay, newYear)
        
        eventName.append(newName)
        eventMonth.append(newMonth)
        eventDay.append(newDay)
        eventYear.append(newYear)
        
        proceed = input("Do you want to enter another event? NO to stop: ")
		
        if (proceed.lower() == 'no'):
            printEvents(eventName, eventMonth, eventDay, eventYear)
            break

#*********** MAIN **********
eventName = []
eventMonth = []
eventDay = []
eventYear = []

addEvent()
