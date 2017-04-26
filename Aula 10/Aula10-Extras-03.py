def read_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número deveser positivo.")
        else:
            return number


def h_value(number):
    h = 0
    for i in range(1, number):
        h += 1 / i
    return h


number = read_number()
print(h_value(number))
