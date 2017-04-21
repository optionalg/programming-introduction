def is_even(number):
    return number % 2 == 0


max_number = int(input("Digite um número: "))
number_of_even_numbers = 0

for i in range(0, max_number):
    if is_even(i):
        print(i)
        number_of_even_numbers += 1


print("Quantidade de números pares: {0}".format(number_of_even_numbers))
