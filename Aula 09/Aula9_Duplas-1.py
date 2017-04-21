"""
Aula 9
Exercícios Duplas 1
Formulário - Idade/Gênero/Estado Civil/Classificação
Autor: Lucien Constantino
"""

def get_age():
    while True:
        age = int(input("Digita sua idade: "))
        if age < 0 or age > 150:
            print("Idade inválida.")
        else:
            return age


def get_salary():
    while True:
        salary = float(input("Digita seu salário: "))
        if salary < 0:
            print("Salário inválido.")
        else:
            return salary


def get_gender():
    while True:
        gender = input("Digita seu gênero (M/F): ")
        if gender != "m" and \
            gender != "M" and \
            gender != "f" and \
            gender != "F":
            print("Gênero inválido.")
        else:
            return gender


def get_marital_status():
    while True:
        marital_status = input("Digite seu estado civil: ")
        if marital_status != "s" and \
            marital_status != "S" and \
            marital_status != "c" and \
            marital_status != "C" and \
            marital_status != "v" and \
            marital_status != "V" and \
            marital_status != "d" and \
            marital_status != "D":

            print("Estado civil inválido.")
        else:
            return marital_status


def get_classification():
    while True:
        classification = input("Digite a classificação: ")
        if classification  != "a" and \
            classification != "A" and \
            classification != "b" and \
            classification != "B" and \
            classification != "c" and \
            classification != "C" and \
            classification != "d" and \
            classification != "D" and \
            classification != "e" and \
            classification != "E":

            print("Classificação inválida.")
        else:
            return classification


age = get_age()
print("Idade: ".format(age))

gender = get_gender()
print("Gênero: ".format(gender))

marital_status = get_marital_status()
print("Estado Civil: ".format(marital_status))

classification = get_classification()
print("Classificação: ".format(classification))
