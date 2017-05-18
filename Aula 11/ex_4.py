"""
Exercício 4
Autor: Lucien Constantino
"""

def get_weight():
    while True:
        weight = float(input("Digite o peso: "))
        if weight < 0:
            print("Peso inválido.")
        else:
            return weight


def get_height():
    while True:
        height = float(input("Digite a altura: "))
        if height <= 0:
            print("Altura inválida.")
        else:
            return height


def get_code():
    n = int(input("Digite o código do cliente"))
    if n < 0:
        print("Número deve ser positivo")
    else:
        return n


class Customer():
    def __init__(self, code, height, weight):
        self.code = code
        self.height = height
        self.weight = weight

    def __eq__(self, other):
        return (self.code == other.code and
                self.height == other.height and
                self.weight == other.weight)


customers: [Customer] = []

while True:
    code = get_code()
    if code == 0:
        break

    height = get_height()
    weight = get_weight()

    customer = Customer(code, height, weight)
    customers.append(customer)


def answers(customers):
    total_heights = 0.0
    total_weights = 0.0

    tallest: Customer = customers[0]
    heaviest: Customer = customers[0]
    shortest: Customer = customers[0]
    lightest: Customer = customers[0]

    for customer in customers:

        if customer.height > tallest.height:
            tallest = customer

        if customer.weight > heaviest.weight:
            heaviest = customer

        if customer.height < shortest.height:
            shortest = customer

        if customer.weight < lightest.weight:
            lightest = customer

        total_heights += customer.height
        total_weights += customer.weight

    number_of_customers = len(customers)
    average_height = total_heights / number_of_customers
    average_weight = total_weights / number_of_customers

    return (tallest, shortest, heaviest, lightest, average_height, average_weight)


tallest = answers(customers)[0]
shortest = answers(customers)[1]
heaviest = answers(customers)[2]
lightest = answers(customers)[3]
average_height = answers(customers)[4]
average_weight = answers(customers)[5]

print("O cliente mais alto tem {0} de altura e código {1}".format(tallest.height, tallest.code))
print("O cliente mais baixo tem {0} de altura e código {1}".format(shortest.height, shortest.code))
print("O cliente mais pesado tem {0} e código {1}".format(heaviest.weight, heaviest.code))
print("O cliente mais leve tem {0} e código {1}".format(lightest.weight, lightest.code))

# TESTING

customer1 = Customer(1, 100, 200)
customer2 = Customer(2, 50, 150)
customer3 = Customer(3, 70, 60)
customers = [customer1, customer2, customer3]

tallest = answers(customers)[0]
shortest = answers(customers)[1]
heaviest = answers(customers)[2]
lightest = answers(customers)[3]
average_height = answers(customers)[4]
average_weight = answers(customers)[5]

assert tallest == customer1
assert shortest == customer2
assert heaviest == customer1
assert lightest == customer3
assert average_weight == (200 + 150 + 60) / 3.0
assert average_height == (100 + 50 + 70) / 3.0
