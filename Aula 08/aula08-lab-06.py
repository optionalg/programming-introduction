"""
Aula 8
Exercício de Laboratório 6
Quociente e Resto sem // ou %
Autor: Lucien Constantino
"""

n1 = int(input("Digite o numerador: "))
n2 = int(input("Digite o denominador: "))

sum = 0
multiplier = 0
quotient = 0

while sum < n1:
  sum += n2
  quotient += 1
    
remainder = n1 - (quotient * n2)

print("Quociente da divisão entre {0} e {1} é: {2}".format(n1, n2, quotient))
print("O resto é: {0}".format(remainder))
