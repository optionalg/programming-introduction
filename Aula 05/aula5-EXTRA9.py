num = input("Type a number with 3 digits: ")

tens = int(num[1])
print(tens)

if tens % 2 == 0:
	print("Even")
else:
	print("Odd")
