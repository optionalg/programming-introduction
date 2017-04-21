number = int(input("Type a number: "))

condition = "not "
if (number % 3 == 0) and (number % 5 == 0):
	condition = ""
	
print("This number is {0}divisible by 3 and 5.".format(condition))
