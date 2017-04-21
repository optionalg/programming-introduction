
min_number = 0
max_number = 4
sum_of_even_numbers = 0

for i in range(min_number, max_number+1, 2):
    sum_of_even_numbers += i

print("Soma dos pares: {0}".format(sum_of_even_numbers))
