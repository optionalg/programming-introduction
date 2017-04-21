"""
Aula 9
Ex. Laboratório 1
Avaliação Cinema
Autor: Lucien Constantino
"""


def get_age():
    while True:
        age = int(input("Digite sua idade: "))
        if age < 14:
            print("Idade não permitida.")
        else:
            return age


def get_rating():
    while True:
        rating = input("Digite sua nota: ")
        if rating != "A" and \
            rating != "B" and \
            rating != "C" and \
            rating != "D" and \
            rating != "E":
            print("Nota inválida.")
        else:
            return rating

cinema_occupation = 100
count = 0
a_answers = 0
sum_ages_with_d_rating = 0
d_ratings = 0
e_answers = 0
oldest_age_b_rating = 0
youngest_age_c_rating = 0
youngest_age_d_rating = 0

while count < cinema_occupation:

    print("====================")

    age = get_age()
    rating = get_rating()

    if rating == "A":
        a_answers += 1

    if rating == "B":
        if age > oldest_age_b_rating:
            oldest_age_b_rating = age

    if rating == "C":
        if youngest_age_c_rating == 0 or age < youngest_age_c_rating:
            youngest_age_c_rating = age

    if rating == "D":
        sum_ages_with_d_rating += age
        d_ratings += 1
        if youngest_age_d_rating == 0 or age < youngest_age_d_rating:
            youngest_age_d_rating = age

    if rating == "E":
        e_answers += 1

    count += 1


print("====================")

print("Quantidade de respotas Ótimo: {0}".format(a_answers))

if d_ratings > 0:
    average_age = sum_ages_with_d_rating / d_ratings
    print("A média de idade das pessoas que responderam Ruim: {0:.1f} anos".format(average_age))

percentage = (e_answers / count) * 100
print("Porcentagem de respostas Péssimo: {0:.1f}%".format(percentage))

print("A maior idade entre as pessoas que responderam Bom: {0} anos".format(oldest_age_b_rating))

print("youngest_age_c_rating: {0}".format(youngest_age_c_rating))
print("youngest_age_d_rating: {0}".format(youngest_age_d_rating))
if youngest_age_c_rating > 0 and youngest_age_d_rating > 0:
    difference = abs(youngest_age_c_rating - youngest_age_d_rating)
    print("Diferença entre a menor idade que respondeu Regular e a menor idade que respondeu Ruim: {0} anos".format(difference))
