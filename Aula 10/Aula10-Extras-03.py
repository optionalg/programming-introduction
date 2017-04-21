def read_number():
    while True:
        number = int(input("Digite um número: "))
        if number < 0:
            print("Número deveser positivo.")
        else:
            return number


number = read_number()


def h_value(number):
    for i in range(1, number):







