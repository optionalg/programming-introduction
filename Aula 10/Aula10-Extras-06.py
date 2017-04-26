def read_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número deve ser positivo.")
        else:
            return number


def divisors_of_number(number):

    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


number = read_number()
divisors_count = len(divisors_of_number(number))
print("Quantidade de divisores de {0} = {1}".format(number, divisors_count))
print("Divisores: {0}".format(divisors_of_number(number)))

assert divisors_of_number(12) == [1, 2, 3, 4, 6, 12]
