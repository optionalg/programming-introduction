import math


def read_number():
    while True:
        number = int(input("Digite um número: "))
        if number <= 0:
            print("Número deve ser maior que 0.")
        else:
            return number


def series_sum(number_of_terms):

    numerator = 100
    terms_sum = 0

    for i in range(number_of_terms):
        denominator = math.factorial(i)
        terms_sum += numerator / denominator
        numerator -= 1
    return terms_sum


n_terms = 20
print("Soma dos {0} primeiros termos da série: {1}".format(n_terms, series_sum(n_terms)))
