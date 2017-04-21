# -*- coding: utf-8 -*-

# Aula 7
# Laboratório
# Exercício 11
# Autor: Lucien Constantino


from enum import Enum

class Quadrant(Enum):
    ORIGIN = 0
    Q1 = 1
    Q2 = 2
    Q3 = 3
    Q4 = 4

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def quadrant(self):
        quadrant = Quadrant.ORIGIN
        if self.x > 0 and self.y > 0:
            quadrant = Quadrant.Q1
        elif self.x < 0 and self.y > 0:
            quadrant = Quadrant.Q2
        elif self.x < 0 and self.y < 0:
            quadrant = Quadrant.Q3
        elif self.x > 0 and self.y < 0:
            quadrant = Quadrant.Q4
        return quadrant


assert Point(0.1, 0.1).quadrant() == Quadrant.Q1
assert Point(-0.1, 0.1).quadrant() == Quadrant.Q2
assert Point(-0.1, -0.1).quadrant() == Quadrant.Q3
assert Point(4.5, -2.2).quadrant() == Quadrant.Q4
assert Point(0.0, 0.0).quadrant() == Quadrant.ORIGIN

def get_point():
    while True:
        try:
            measures_input = input("Digite as coordenadas x e y - separados por espaço: ")
        except (NameError, ValueError, AttributeError, UnboundLocalError):
            print("Valor inválido.")
            continue

        measures_input = measures_input.split()

        if len(measures_input) != 2:
            print("Digite apenas X e Y.")
            continue

        measures = list(map(float, measures_input))
        break

    return Point(measures[0], measures[1])

point = get_point()
print(point.quadrant())
