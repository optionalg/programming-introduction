"""
Aula 8
Exercício de Laboratório 7
x ** n
Autor: Lucien Constantino
"""

x = int(input("Digite x: "))
n = int(input("Digite n: "))
count = 0
mult = 1

while count < n:
  mult *= x
  count += 1
  
print("x^n == {0}".format(mult))

