regionCode = int(input("Código da Região: "))
unitsSold = int(input("Unidades: "))
unitCost = 7

def shippingCostPerUnit(region, units, unitCost):
	shippingCostPerUnit = 0
		
	if region == 1:
		if units <= 1000:
			shippingCostPerUnit = 1
		else:
			shippingCostPerUnit = unitCost * 0.1
	elif region == 2:
		if units <= 1000:
			shippingCostPerUnit = 1.1
		else:
			shippingCostPerUnit = unitCost * 0.08
	elif region == 3:
		if units <= 1000:
			shippingCostPerUnit = 1.15
		else:
			shippingCostPerUnit = unitCost * 0.07
	elif region == 4:
		if units <= 1000:
			shippingCostPerUnit = 1.2
		else:
			shippingCostPerUnit = unitCost * 0.11
	elif region == 5:
		if units <= 1000:
			shippingCostPerUnit = 1.25
		else:
			shippingCostPerUnit = unitCost * 0.15
	elif region == 6:
		if units <= 1000:
			shippingCostPerUnit = 1.3
		else:
			shippingCostPerUnit = unitCost * 0.12
	elif region == 7:
		if units <= 1000:
			shippingCostPerUnit = 1.4
		else:
			shippingCostPerUnit = unitCost * 0.18
	elif region == 8:
		if units <= 1000:
			shippingCostPerUnit = 1.35
		else:
			shippingCostPerUnit = unitCost * 0.15
			
	return shippingCostPerUnit
		
shippingCost = unitsSold * shippingCostPerUnit(regionCode, unitsSold, unitCost)
totalCost = unitsSold * unitCost
revenue = totalCost * 1.5
sellerCommission = revenue * 0.065
profit = revenue - totalCost - sellerCommission

# Valor do frete?
print("Frete = R${0:.2f}".format(shippingCost))
# Comissão do vendedor?
print("Comissão do vendedor = R${0:.2f}".format(sellerCommission))
# Lucro Obtido com a venda?
print("Lucro = R${0:.2f}".format(profit))
