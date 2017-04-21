# Condições de Pagamento Loja

operation = int(input("Operação (1/2/3/4): "))
price = float(input("Preço: "))

def paymentType(operation, price):
	amount = 0
	slips = 1
	if operation == 1:
		amount = price * (1 - 0.1)
	elif operation == 2:
		amount = price * (1 - 0.05)
	elif operation == 3:
		slips = 2
		amount = price / slips
	elif operation == 4:
		slips = 3
		amount = (price * 1.1) / slips
		
	return [slips, amount]

payment = paymentType(operation, price)

print("Valor a pagar: {0} de R${1:.2f}".format(payment[0], payment[1]))

