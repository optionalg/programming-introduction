import math
# Aula 4
# Exercício Laboratório 1
print("This program calculates the volume of a cilinder.")
radius = float(input("Type the radius of the cilinder: "))
height = float(input("Type the height of the cilinder: "))

def cilinderVolume(radius, height):
	volume = math.pi * math.pow(radius, 2) * height
	return volume

result = cilinderVolume(radius, height)
print("x1 = {0:.2f}".format(result))

