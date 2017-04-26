def get_age():
    while True:
        age = int(input("Digite a idade: "))
        if age < 1:
            print("Idade inválida.")
        else:
            return age


def get_weight():
    while True:
        weight = float(input("Digite o peso: "))
        if weight < 0:
            print("Peso inválido.")
        else:
            return weight


def get_height():
    while True:
        height = float(input("Digite a altura: "))
        if height <= 0:
            print("Altura inválida.")
        else:
            return height


class Person:

    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


number_of_people = 2
people = []

for i in range(number_of_people):

    person = Person(get_age(), get_weight(), get_height())
    people.append(person)


elder_people = 0
sum_height_teenagers = 0.0
number_of_teenagers = 0
lightweight_people = 0

for person in people:

    if person.age > 50:
        elder_people += 1

    if person.age > 10 and person.age < 20:
        number_of_teenagers += 1
        sum_height_teenagers += person.height

    if person.weight < 40:
        lightweight_people += 1


print("Pessoas com idade superior a 50 anos: {0}".format(elder_people))

if number_of_teenagers > 0:
    average_height_teenagers = sum_height_teenagers / number_of_teenagers
    print("Média das alturas das pessoas com idade entre 10 e 20 anos: {0}".format(average_height_teenagers))

lightweight_people_percentage = (lightweight_people / number_of_people) * 100
print("% de pessoas com peso inferior a 40 Kg entre todas: {0:.1f}".format(lightweight_people_percentage))
