sum = 0
numerator = 1
denominator = 1

for numerator in range(1, 100, 2):
    term = numerator / denominator
    denominator += 1
    sum += term


print(sum)


