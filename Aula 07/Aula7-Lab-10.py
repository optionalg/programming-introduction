#!/usr/bin/python
# -*- coding: utf-8 -*-

# Aula 7
# Laboratório
# Exercício 10
# Autor: Lucien Constantino


def deltaPressure(target, current):
    return target - current

targetPressure = int(input())
currentPressure = int(input())

assert deltaPressure(30, 18) == 12
assert deltaPressure(27, 27) == 0
assert deltaPressure(27, 30) == -3

print (deltaPressure(targetPressure, currentPressure))

