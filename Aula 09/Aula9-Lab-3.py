"""
Aula 9
Ex. Laboratório 3
Pesquisa Times de Futebol, Cidade, Salário
Autor: Lucien Constantino
"""


from enum import Enum


class SoccerTeam(Enum):
    SAO_PAULO = 1
    CORINTHIANS = 2
    SANTOS = 3
    OTHER = 4


class Place(Enum):
    SAOPAULO = 1
    LITORAL = 2
    INTERIOR = 3


class Person:

    def __init__(self, soccer_team, place_you_live, salary):
        self.soccer_team = soccer_team
        self.place_you_live = place_you_live
        self.salary = salary


poll_count = 2
persons = []
minimum_wage = float(input("Informe o valor do salário mínimo: R$ "))


def get_soccer_team():
    while True:
        print("Qual seu time do coração? ")
        print("1 - São Paulo")
        print("2 - Corinthians")
        print("3 - Santos")
        print("4 - Outros")

        soccer_team = int(input())
        if soccer_team < 1 or soccer_team > 4:
            print("Opção inválida.")
        else:
            return SoccerTeam(soccer_team)


def get_place():
    while True:
        print("Onde você mora?")
        print("1 - São Paulo")
        print("2 - Litoral")
        print("3 - Interior")

        place = int(input())
        if place < 1 or place > 3:
            print("Opção inválida.")
        else:
            return Place(place)


def get_salary():
    while True:
        print("Qual o seu salário? ")
        salary = float(input())
        if salary < minimum_wage:
            print("Salário deve ser pelo menos o salário mínimo.")
        else:
            return salary


while len(persons) < poll_count:

    print("=================")

    soccer_team = get_soccer_team()
    place = get_place()
    salary = get_salary()

    persons.append(Person(soccer_team, place, salary))


fans = [0, 0, 0, 0]  # São Paulo, Corinthians, Santos, Outros
sum_salaries_sao_paulo_fans = 0
corinthians_fans_living_in_sao_paulo = 0
santos_fans_living_in_litoral = 0

for person in persons:

    fans[person.soccer_team.value-1] += 1

    if person.soccer_team == SoccerTeam.SAO_PAULO:
        sum_salaries_sao_paulo_fans += person.salary

    if person.soccer_team == SoccerTeam.CORINTHIANS and person.place_you_live == Place.SAOPAULO:
        corinthians_fans_living_in_sao_paulo += 1

    if person.soccer_team == SoccerTeam.SANTOS and person.place_you_live == Place.LITORAL:
        santos_fans_living_in_litoral += 1


def get_question_menu():
    while True:
        print("1. Número de torcedores por clube:")
        print("2. Média salarial dos torcedores do São Paulo")
        print("3. Número de pessoas moradoras de São Paulo, torcedoras do Corinthians")
        print("4. Número de pessoas do Litoral torcedoras do Santos")
        print("5. Sair")
        question = int(input())
        if question < 1 or question > 5:
            print("Opção inválida")
        else:
            return question


while True:
    print("=================")
    question = get_question_menu()

    if question == 1:
        print("São Paulo: {0}".format(fans[SoccerTeam.SAO_PAULO.value-1]))
        print("Corinthians: {0}".format(fans[SoccerTeam.CORINTHIANS.value-1]))
        print("Santos: {0}".format(fans[SoccerTeam.SANTOS.value-1]))
        print("Outros: {0}".format(fans[SoccerTeam.OTHER.value-1]))
    elif question == 2:
        sao_paulo_fans = fans[SoccerTeam.SAO_PAULO.value-1]
        if sao_paulo_fans > 0:
            q2_result = sum_salaries_sao_paulo_fans / sao_paulo_fans
            print("R${0:.2f}".format(q2_result))
        else:
            print("R${0:.2f}".format(0))
    elif question == 3:
        print(corinthians_fans_living_in_sao_paulo)
    elif question == 4:
        print(santos_fans_living_in_litoral)
    elif question == 5:
        break
