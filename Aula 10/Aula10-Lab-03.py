
n = int(input("Digite um número: "))
s = 0

for numerator in range(1, n + 1):
    denominator = numerator - (numerator - 1)
    term = numerator / denominator
    s += term

print(s)
