import math
num = int(input("Type a number: "))

if num >= 0:
	result = math.sqrt(num)
else:
	result = math.pow(num, 2)

print("Result: {0}".format(result))
