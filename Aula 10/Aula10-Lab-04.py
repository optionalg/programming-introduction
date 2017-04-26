def get_number():
    n = int(input("Digite um número "))
    if n < 0:
        print("Número deve ser positivo")
    else:
        return n


n = get_number()
multiplier = 1
for i in range(1, n + 1):
    multiplier *= i

print(multiplier)
