"""
Aula 9
Exercícios Extras 2
Campeonato Futebol
Autor: Lucien Constantino
"""


def get_age():
    while True:
        age = int(input("Digite a idade (entre 14 e 35): "))
        if age < 14 or age > 35:
            print("Idade inválida.")
        else:
            return age


def get_weight():
    while True:
        weight = float(input("Digite o peso (entre 60.0 a 100.0): "))
        if weight < 60 or weight > 100:
            print("Peso inválido.")
        else:
            return weight


def get_height():
    while True:
        height = float(input("Digite a altura (entre 1.60 e 2.00): "))
        if height < 1.6 or height > 2:
            print("Altura inválida.")
        else:
            return height


team_count = 0
number_of_teams = 3

players_per_team = 2

# questions
underage_player_count = 0
sum_of_heights_all_players = 0
overweight_players = 0

while team_count < number_of_teams:

    print("*** Time {0} ***".format(team_count + 1))
    sum_of_ages_per_team = 0
    player_count = 0

    while player_count < players_per_team:

        print("=== Jogador {0} ===".format(player_count + 1))
        age = get_age()
        weight = get_weight()
        height = get_height()

        if age < 18:
            underage_player_count += 1
        sum_of_ages_per_team += age

        sum_of_heights_all_players += height

        if weight > 80:
            overweight_players += 1

        player_count += 1

    team_count += 1
    print("Média de idade dos jogadores do time {0}: {1:.1f} anos".format(team_count, sum_of_ages_per_team / players_per_team))

print("==========================")
print("Quantidade de jogadores menores de idade: {0}".format(underage_player_count))

total_number_of_players = number_of_teams * players_per_team
average_height_players = sum_of_heights_all_players / total_number_of_players
print("Média das alturas de todos os jogadores: {0:.2f}m".format(average_height_players))
print("Porcentagem de jogadores com mais de 80Kg: {0:.1f}".format((overweight_players / total_number_of_players) * 100))
