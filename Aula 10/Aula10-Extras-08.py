
number_list = []

for i in range(2):
    number_list.append(int(input("Digite um número: ")))


def sum_of_even_positive_numbers(numbers):
    asum = 0
    for number in numbers:
        if number > 0 and number % 2 == 0:
            asum += number
    return asum


print(sum_of_even_positive_numbers(number_list))
