# Laboratório de Programação
# 14/02/2017

import math

def areaOfCircleWithRadius(radius):
	return math.pi * pow((float(radius)), 2)
	
print("This program calculates the area of a circle from the radius.")
radius = input("Radius: ")
print("{0:.2f}".format(areaOfCircleWithRadius(radius)))

