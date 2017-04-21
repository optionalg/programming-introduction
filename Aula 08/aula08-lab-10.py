"""
Aula 8
Exercício de Laboratório 10
MDC
Autor: Lucien Constantino
"""

def mdc(a, b):
  while b != 0:
    q = a / b
    r = a % b
    a = b
    b = r
  return a

assert mdc(252, 105) == 21
assert mdc(147, 105) == 21
assert mdc(348, 156) == 12

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
result = int(mdc(a, b))
print("O MDC entre {0} e {1} é: {2}".format(a, b, result))
