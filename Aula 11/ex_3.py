"""
Exercício 3
Autor: Lucien Constantino
"""

def get_number():
    n = int(input("Digite um número "))
    if n < 0:
        print("Número deve ser positivo")
    else:
        return n


def is_number_triangular(number):
    a = 1
    b = 2
    c = 3
    result = 0

    while result < number:
        result = a * b * c
        print(result)
        if result == number:
            return True
        a += 1
        b += 1
        c += 1

    return False


n = get_number()
if is_number_triangular(n):
    print("O número {0} é triangular.".format(n))
else:
    print("O número {0} não é triangular.".format(n))

assert is_number_triangular(120) == True
