#!/usr/bin/python
# -*- coding: utf-8 -*-

# Aula 7
# Laboratório
# Exercício 8
# Autor: Lucien Constantino


def get_ball_diameter():

    while True:
        try:
            diameter = int(input("Digite o diâmetro da bola de boliche: "))
        except NameError:
            print("Valor inválido.")
            continue

        if diameter < 1 or diameter > 10000:
            print("Diâmetro deve ser maior ou igual a 1, menor ou igual a 10.000")
            continue
        else:
            break
    return diameter


def get_box_dimensions():
    while True:
        try:
            measures_input = input("Digite a altura, largura e profundidade - separados por espaço: ")
        except (NameError, ValueError, AttributeError, UnboundLocalError):
            print("Valor inválido.")
            continue

        measures_input = measures_input.split()

        if len(measures_input) != 3:
            print("É preciso digitar apenas Altura, largura e profundidade.")
            continue

        measures = map(int, measures_input)
        for measure in measures:
            if measure < 1 or measure > 10000:
                print("Altura, largura e profundidade devem ser maiores ou igual a 1, menores ou igual a 10.000")
                continue

        break
    return measures


def fits_inside_box(box_measures, ball_diameter):
    fits = True
    for measure in box_measures:
        if ball_diameter > measure:
            fits = False
            break
    return fits

assert fits_inside_box([3, 2, 5], 3) is False
assert fits_inside_box([5, 5, 5], 5) is True
assert fits_inside_box([15, 9, 10], 9) is True
assert fits_inside_box([10, 20, 30], 100) is False

ball_diameter = get_ball_diameter()
box_measures = get_box_dimensions()

result = ""
if fits_inside_box(box_measures, ball_diameter):
    result = "S"
else:
    result = "N"
print(result)
