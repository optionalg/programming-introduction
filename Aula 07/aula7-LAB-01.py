# Custos Hospital

days = int(input("Número de dias: "))
roomType = input("Tipo de quarto (P, S ou C): ")
wifiUsed = bool(input("Usou Wi-Fi? (0 = Não, 1 = Sim): "))
cableTVUsed = bool(input("Usou TV a cabo? (0 = Não, 1 = Sim): "))

dailyRoomCost = 0
if roomType == "P":
	dailyRoomCost = 360
elif roomType == "S":
	dailyRoomCost = 210
elif roomType == "C":
	dailyRoomCost = 185

roomCost = dailyRoomCost * days

wifiCost = 0
if wifiUsed:
	wifiCost = 3

tvCost = 0
if cableTVUsed:
	tvCost = 4

totalCost = roomCost + wifiCost + tvCost
print("Custo total = {0:.2f}".format(totalCost))

