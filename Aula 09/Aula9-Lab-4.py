"""
Aula 9
Ex. Laboratório 4
Soma de pares
Autor: Lucien Constantino
"""


def get_pair():
    while True:
        pair_input = input("Digite o par: ")
        pair = pair_input.split(",")
        if len(pair) != 2:
            print("Números inválidos")
        else:
            return pair


while True:
    pair = get_pair()
    m = int(pair[0])
    n = int(pair[1])
    if m >= n:
        break

    sum = 0
    for i in range(m, n+1):
        sum += i

    print("Soma = {0}".format(sum))
