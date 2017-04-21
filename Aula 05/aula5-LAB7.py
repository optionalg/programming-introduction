carYear = int(input("Type the year of the car: "))
carCost = float(input("Type the cost of the car: "))

isCarOld = False
if carYear < 2010:
	isCarOld = True

tax = 0.025
if isCarOld:
	tax = 0.035

result = carCost * tax
print("The tax to pay is {0:.2f}".format(result)) 
