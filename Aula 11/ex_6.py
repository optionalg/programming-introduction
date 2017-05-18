"""
Exercício 6
Autor: Lucien Constantino
"""

def get_number():
    while True:
        n = int(input("Digite um número inteiro positivo: "))
        if n < 0:
            print("Número deve ser positivo")
        else:
            return n


number = get_number()
divisions = 0

for i in range(number):

    divisors = 0
    test_num = 1

    while test_num <= i:

        divisions += 1
        if i % test_num == 0:
            divisors += 1
        test_num += 1

    if divisors == 2:
        # prime
        print("Primo: {0}".format(i))

print("Divisões efetuadas: {0}".format(divisions))
