import math
# Aula 4
# Exercício Laboratório 2

x = float(input("Type x: "))
y = float(input("Type y: "))
z = float(input("Type z: "))

result = math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)
print("x^2 + y^2 + z^2 = {0:.2f}".format(result))

result = math.pow((x + y + z), 2)
print("(x + y + z)^2 = {0:.2f}".format(result))
