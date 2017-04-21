"""
Aula 9
Ex. Laboratório 2
Height, Gender Stats
Autor: Lucien Constantino
"""


from enum import Enum, auto


def get_height():
    while True:
        height = float(input("Digite a altura (entre 1.00m e 2.30m): "))
        if height < 1 or height > 2.3:
            print("Altura inválida.")
        else:
            return height


def get_gender():
    while True:
        gender_string = input("Digita seu gênero (M/F): ")

        try:
            gender = gender_from_string(gender_string)
        except ValueError as e:
            print(e)
            continue
        else:
            return gender


class Gender(Enum):
    FEMALE = auto()
    MALE = auto()


def gender_from_string(gender_str):
    if gender_str == "m" or gender_str == "M":
        return Gender.MALE
    if gender_str == "f" or gender_str == "F":
        return Gender.FEMALE
    else:
        raise ValueError("Gênero inválido.")


def get_number_of_people():
    while True:
        n = int(input("Digite o número de pessoas (entre 1 e 50): "))
        if n < 1 or n > 50:
            print("Número inválido.")
        else:
            return n


people_count = 0
min_height = 0
max_height = 0
woman_heights_sum = 0
woman_count = 0
men_count = 0
n_people = get_number_of_people()

while people_count < n_people:

    print("========================")

    height = get_height()
    gender = get_gender()

    if min_height == 0 or height < min_height:
        min_height = height

    if height > max_height:
        max_height = height

    if gender == Gender.FEMALE:
        woman_count += 1
        woman_heights_sum += height

    if gender == Gender.MALE:
        men_count += 1

    people_count += 1


print("========================")
print("Maior altura: {0:.1f}".format(max_height))
print("Menor altura: {0:.1f}".format(min_height))

average_height_woman = woman_heights_sum / woman_count
print("A média de altura das mulheres: {0:.1f}m".format(average_height_woman))

print("Número de homens: {0}".format(men_count))
