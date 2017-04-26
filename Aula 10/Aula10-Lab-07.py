def get_number():
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número deve ser positivo")
    else:
        return n


def factorial(number):
    multiplier = 1
    for i in range(1, number + 1):
        multiplier *= i
    return multiplier


for n in range(get_number()):

    term = get_number()
    print("{0}! = {1}".format(term, factorial(term)))
