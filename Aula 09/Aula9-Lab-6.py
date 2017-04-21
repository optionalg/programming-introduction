"""
Aula 9
Ex. Laboratório 6
Primo
Autor: Lucien Constantino
"""


def get_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número inválido")
        else:
            return number


def is_prime(number):
    divisors = 0
    test_num = 1

    while test_num <= number:

        if number % test_num == 0:
            divisors += 1
        test_num += 1

    return divisors == 2


number = get_number()
if is_prime(number):
    print("Primo")
else:
    print("Não é primo")
