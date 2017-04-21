"""
Aula 9
Ex. Laboratório 7
Fatorial
Autor: Lucien Constantino
"""


def get_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número inválido")
        else:
            return number


def factorial(number):
    multiplication = 1
    count = 1
    while count <= number:
        multiplication *= count
        count += 1
    return multiplication


n = get_number()

message = ""
for i in range(0, n):
    if i == n-1:
        message += "{0}".format(n-i)
    else:
        message += "{0} x ".format(n-i)


print("{0}! = {1} = {2}".format(n, message, factorial(n)))



