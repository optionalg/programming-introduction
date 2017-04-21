kwHourPrice = float(input("Preço do KW/hora: "))
kwHourConsumption = float(input("KW/hora consumidos no mês: "))
consumerType = input("Tipo de consumidor (I = Industrial, C = Comercial, R = Residencial): ")

bonus = 0
if consumerType == "I":
	bonus = 1.15
elif consumerType == "C":
	bonus = 1.05

cost = (kwHourConsumption * kwHourPrice) * bonus
print("Custo de energia elétrica no mês: {0:.2f}".format(cost))
