import math
# Aula 4
# Exercício Lab 3
print("This program converts a date in the format aaaammdd to the format dd/mm/yyyy")
date = input("Type the date in the format aaaammdd: ")

def dateBrazilianFormat(date):
	year = date[0:4]
	month = date[4:6]
	day = date[6:8]
	return "{0}/{1}/{2}".format(day, month, year)

print(dateBrazilianFormat(date))
