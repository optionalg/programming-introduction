"""
Exercício 2
Autor: Lucien Constantino
"""

def get_number():
    n = int(input("Digite um número "))
    if n < 0:
        print("Número deve ser positivo")
    else:
        return n

def divisors_of_number(number):

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(number):
    sum = 0
    for divisor in divisors_of_number(number):
        sum += divisor
    return sum == number

n = get_number()
if is_perfect_number(n):
    print("{0} é um número perfeito.".format(n))
else:
    print("{0} não é um número perfeito.".format(n))
