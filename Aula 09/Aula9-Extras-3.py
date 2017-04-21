"""
Aula 9
Exercícios Extras 3
Caixa Registradora
Autor: Lucien Constantino
"""


def get_price(message):
    while True:
        price = float(input(message))
        if price < 0:
            print("Valor inválido.")
        else:
            return price


product_count = 0
total = 0

while True:

    price = get_price("Produto {0}: R$ ".format(product_count + 1))
    if price == 0:
        break

    total += price
    product_count += 1


print("=====================================")
print("Total: R$ {0:.2f}".format(total))
cash = get_price("Dinheiro: R$ ")

if cash < total:
    amount_owned = total - cash
    print("Ainda falta R$ {0:.2f}".format(amount_owned))
else:
    change = cash - total
    print("Troco R$ {0:.2f}".format(change))
