"""
Exercício 1
Autor: Lucien Constantino
"""

population_country_A = 80000
annual_growth_rate_A = 0.03

population_country_B = 200000
annual_growth_rate_B = 0.015

year = 0
while population_country_A < population_country_B:

    population_country_A += population_country_A * annual_growth_rate_A
    population_country_B += population_country_B * annual_growth_rate_B
    year += 1

print("São necessários {0} anos para que o país A iguale ou ultrapasse o país B em população.".format(year))
