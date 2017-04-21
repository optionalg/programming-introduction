"""
Aula 8
Exercício de Laboratório 5
Multiplicação sem *
Autor: Lucien Constantino
"""

n1 = int((input("Digite um número: ")))
n2 = int((input("Digite outro número: ")))
sum = 0

count = 0
while count < n2:
  sum += n1
  count += 1
  
print("{0} * {1} = {2}".format(n1, n2, sum))
  
