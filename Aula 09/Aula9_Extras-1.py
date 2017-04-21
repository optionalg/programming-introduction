"""
Aula 9
Exercícios Extras 1
Pesquisa: Gênero/Idade/Quantidade/Percentual
Autor: Lucien Constantino
"""

from enum import Enum, auto

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


def get_signup_id():
    while True:
        signup_id = int(input("Digite o número de inscrição: "))
        if signup_id < 0 or signup_id > 9999:
            print("Número de inscrição inválido.")
        else:
            return signup_id


def get_age():
    while True:
        age = int(input("Digite a idade: "))
        if age < 16 or age > 60:
            print("Idade inválida.")
        else:
            return age


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


def get_work_experience():
    while True:
        has_experience = input("Possui experiência? (S/N): ")
        if has_experience == "S":
            return True
        elif has_experience == "N":
            return False
        else:
            print("Comando inválido")
            continue


signup_counts = 0
woman_count = 0
men_count = 0
age_sum_for_men_with_experience = 0
men_avobe_45 = 0
young_woman_with_experience = 0
youngest_age_woman_with_experience = 0

while True:
    signup_id = get_signup_id()
    if signup_id == 0:
        break
    signup_counts += 1

    age = get_age()
    gender = get_gender()

    has_experience = get_work_experience()

    # Quantidade de homens
    if gender == Gender.MALE:
        men_count += 1
        if has_experience:
            age_sum_for_men_with_experience += age
        if age > 45:
            men_avobe_45 += 1

    if gender == Gender.FEMALE:
        woman_count += 1
        if has_experience:
            if age < 35:
                young_woman_with_experience += 1

            if signup_counts == 1:
                youngest_age_woman_with_experience = age
            elif age < youngest_age_woman_with_experience:
                youngest_age_woman_with_experience = age


print("Quantidade de homens: {0}".format(men_count))
woman_count = signup_counts - men_count
print("Quantidade de mulheres: {0}".format(woman_count))

if men_count > 0:
    average_age_for_men_with_experience = int(age_sum_for_men_with_experience / men_count)
    print("Idade média dos homens que já tem experiência de serviço: {0}".format(average_age_for_men_with_experience))
    print("Percentual de homens com mais de 45 anos entre o total de homens: {0:.1f}%".format((men_avobe_45 / men_count) * 100))

if woman_count > 0:
    print("Número de mulheres que têm idade inferior a 35 anos e com experiência no serviço: {0:.1f}%".format((young_woman_with_experience / woman_count) * 100))

if youngest_age_woman_with_experience > 0:
    print("A menor idade entre mulheres que já têm experiência no serviço: {0}".format(youngest_age_woman_with_experience))
