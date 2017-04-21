import math
pesoPeixes = float(input("Digite o peso dos peixes:"))

excedente = 0
if pesoPeixes > 50:
	excedente = pesoPeixes - 50
	print("Peso excedente: {0:.1f}".format(excedente))
	multa = math.ceil(excedente) * 4
	print("Multa = {0:.2f}".format(multa))
else:
	print("Dentro do regulamento")


