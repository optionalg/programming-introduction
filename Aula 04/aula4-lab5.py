import math
# Aula 4
# Exercício Laboratorio 5

productCost = int(input("Type the price of the product: "))

hundredBills = int(productCost / 100)
productCost = productCost - (hundredBills * 100)

fiftyBills = int(productCost / 50)
productCost = productCost - (fiftyBills * 50)

twentyBills = int(productCost / 20)
productCost = productCost - (twentyBills * 20)

tenBills = int(productCost / 10)
productCost = productCost - (tenBills * 10)

fiveBills = int(productCost / 5)
productCost = productCost - (fiveBills * 5)

twoBills = int(productCost / 2)
productCost = productCost - (twoBills * 2)

oneBills = int(productCost / 1)
productCost = productCost - (oneBills * 1)

print("Bills of 100: {0}".format(hundredBills))
print("Bills of 50: {0}".format(fiftyBills))
print("Bills of 20: {0}".format(twentyBills))
print("Bills of 10: {0}".format(tenBills))
print("Bills of 5: {0}".format(fiveBills))
print("Bills of 2: {0}".format(twoBills))
print("Bills of 1: {0}".format(oneBills))

