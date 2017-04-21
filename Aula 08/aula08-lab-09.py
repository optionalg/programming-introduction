"""
Aula 8
Exercício de Laboratório 9
MMC
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
  
def mmc(a, b):
  return (a * b) / mdc(a, b)
  
assert mmc(21, 6) == 42

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print("O MMC entre a e b é: {0}".format(int(mmc(a, b))))
