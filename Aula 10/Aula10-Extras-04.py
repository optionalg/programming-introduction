def read_number():
    while True:
        number = int(input("Digite um número: "))
        if number <= 0:
            print("Número deve ser maior que 0.")
        else:
            return number


def fibonacci_series(n):

    seed_f1 = 1
    seed_f2 = 1
    series = [seed_f1]

    if n == 1:
        return series
    else:
        series.append(seed_f2)
        if n == 2:
            return series

    for i in range(n-2):
        fn = seed_f1 + seed_f2
        seed_f1 = seed_f2
        seed_f2 = fn
        series.append(fn)
    return series


n_term = read_number()
print(fibonacci_series(n_term))
