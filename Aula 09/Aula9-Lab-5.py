"""
Aula 9
Ex. Laboratório 5
Taboada
Autor: Lucien Constantino
"""


def get_value(message):
    while True:
        value = int(input("Valor {0} = ".format(message)))
        if value < 0:
            print("Valor inválido.")
        else:
            return value

initial_value = get_value("inicial")
final_value = get_value("final")

for taboada_num in range(initial_value, final_value+1):

    print("==================")
    print("Tabuada de {0}".format(taboada_num))
    for i in range(0, 10):
        multiplication = taboada_num * (i+1)
        print("{0} x {1} = {2}".format(taboada_num, i+1, multiplication))
