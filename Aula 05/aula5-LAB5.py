year = int(input("Type a year: "))

def isLeapYear(year):
	isLeapYear = False
	if year % 400 == 0:
		isLeapYear = True
	elif year % 4 == 0 and year % 100 != 0:
		isLeapYear = True
	return isLeapYear


condition = "" if isLeapYear(year) else "not "
print("This is {0}a leap year.".format(condition))

assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(1600) == True
assert isLeapYear(1601) == False
assert isLeapYear(1996) == True
assert isLeapYear(1997) == False
assert isLeapYear(2004) == True
assert isLeapYear(2005) == False
assert isLeapYear(2012) == True
assert isLeapYear(2013) == False
assert isLeapYear(2017) == False
