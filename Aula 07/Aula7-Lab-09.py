#!/usr/bin/python
# -*- coding: utf-8 -*-

# Aula 7
# Laboratório
# Exercício 9
# Autor: Lucien Constantino


def water_bill_amount(cubic_meters):

    tier0 = 10
    tier1 = 30
    tier2 = 100
    tier3 = cubic_meters

    tier_1_consumption = 0
    tier_2_consumption = 0
    tier_3_consumption = 0

    if cubic_meters > tier0:
        if  cubic_meters - tier1 > 0:
            tier_1_consumption = tier1 - tier0
        else:
            tier_1_consumption = cubic_meters - tier0

    if cubic_meters > tier1:
        if cubic_meters - tier2 > 0:
            tier_2_consumption = tier2 - tier1
        else:
            tier_2_consumption = cubic_meters - tier1

    if cubic_meters > tier2:
        tier_3_consumption = cubic_meters - tier2

    return 7 + (tier_1_consumption * 1) + (tier_2_consumption * 2) + (tier_3_consumption * 5)

assert water_bill_amount(120) == 267
assert water_bill_amount(8) == 7
assert water_bill_amount(14) == 11
assert water_bill_amount(42) == 51

water_consumption = int(input())
print(water_bill_amount(water_consumption))
