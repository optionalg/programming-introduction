"""
Aula 9
Ex. Laboratório 7
Primos entre 1 e N
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


n = get_number()
count = 1

while count <= n:
    if is_prime(count):
        print(count)
    count += 1
