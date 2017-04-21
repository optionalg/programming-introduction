# -*- coding: utf-8 -*-

# Aula 7
# Laboratório
# Exercício 11
# Autor: Lucien Constantino


class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

products = [Product("1", "Cachorro Quente", 400),
            Product("2", "X-Salada", 450),
            Product("3", "X-Bacon", 500),
            Product("4", "Torrada simples", 200),
            Product("5", "Refrigerante", 150)]


class Purchase:
    def __init__(self, code, quantity):
        self.quantity = quantity
        self.product = products[code-1]

    @property
    def total_in_cents(self):
        total_in_cents = self.product.price * self.quantity
        return total_in_cents

    def localized_total(self):
        total_in_reais = self.total_in_cents / 100.0
        return "Total: R$ {0:.2f}".format(total_in_reais)

    def localized_string(self):
        return "{0}x {1}".format(self.quantity, self.product.name)

assert Purchase(3, 2).total_in_cents == 1000
assert Purchase(4, 3).total_in_cents == 600
assert Purchase(2, 3).total_in_cents == 1350


def get_code_and_quantity():
    while True:
        try:
            item_input = input("Digite o código do item e a quantidade do mesmo separados por espaço: ")
        except (NameError, ValueError, AttributeError, UnboundLocalError):
            print("Valores inválidos.")
            continue

        item_info = item_input.split()

        if len(item_info) != 2:
            print("Digite apenas o código e quantidade do produto.")
            continue

        item_info = list(map(int, item_info))

        code = item_info[0]
        if code < 1 or code > 5:
            print("Código deve ser entre 1 e 5.")
            continue

        break

    return item_info


item_info = get_code_and_quantity()
purchase = Purchase(item_info[0], item_info[1])
print(purchase.localized_string())
print(purchase.localized_total())
