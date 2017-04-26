start = int(input("Digite um valor inicial: "))

while True:
    end = int(input("Digite um valor final: "))
    if end < start:
        print("Valor final deve ser maior que o valor inicial")
    else:
        break


def sum_of_integers(start, finish):
    sum = 0
    for i in range(start + 1, finish):
        sum += i
    return sum


print(sum_of_integers(start, end))

assert sum_of_integers(1, 6) == 14


