# Laboratorio de Programação
# 14/02/2017

def monthlyWageFrom(hoursWorkedInMonth, wagePerHour):
	return int(hoursWorkedInMonth) * int(wagePerHour)
	
print("This program calculates your monthly salary.")
wagePerHour = input("Hourly salary: ")
hours = input("Number of hours you've worked in the month: ")

print(monthlyWageFrom(hours, wagePerHour))

	
