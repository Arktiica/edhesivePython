# Check for and adjust month input if necessary
def validateMonth(month):
	if (month > 12 or month < 1):
		month = 1
	return month

def validateDay(month, day, year):
	leap = 0
	if (year % 4 == 0):
		leap = 1
	if (year % 100 == 0 and year % 400 != 0):
		leap = 0
	if (day < 1 or day > 31):
		day = 1
	if (month == 4 or month == 6 or month == 9 or month == 11):
		if (day > 30):
			day = 1
	if (month == 2):
		if (leap == 1 and day > 29):
			day == 1
		elif (leap == 0 and day > 28):
			day == 1
	return day
		

# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def printEvents(eventName, eventMonth, eventDay, eventYear):
	months = ['January','February','March','April','May','June','July','August', 'September','October','November','December']
	print("******************** List of Events ********************")
	for i in range(len(eventName)):
		print(eventName[i])
		print("Date: " + str(months[eventMonth[i]-1]) + " " + str(eventDay[i]) + ", " + str(eventYear[i]))

# This function is used to prompt, adjust and
# append values to the 4 parallel arrays
def addEvent():
    while (True):
        newName = input("What is the event: ")
        newMonth = int(input("What is the month (number): "))
        newDay = int(input("What is the day: "))
        newYear = int(input("What is the year: "))
        print("")


        eventName.append(newName)
        eventMonth.append(validateMonth(newMonth))
        eventDay.append(validateDay(newMonth, newDay, newYear))
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
