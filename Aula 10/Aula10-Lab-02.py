import math

def get_number():
    n = int(input("Digite um número: "))
    if n < 1 or n > 20:
        print("Número inválido, digite um número entre 1 e 20 inclusives")
    return n


n = get_number()

for i in range(1, n + 1):
    print(math.pow(i, 2))
