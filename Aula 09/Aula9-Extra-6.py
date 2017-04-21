"""
Aula 9
Exercícios Extras 6

Autor: Lucien Constantino
"""


def get_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número inválido")
        else:
            return number


n = get_number()
count = 0
number_count = 10

while count < n:

    line = ""
    for i in range(0, number_count):
        line += "{0} ".format(i)
    print(line)
    number_count -= 1
    count += 1




