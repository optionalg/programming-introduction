"""
Aula 8
Exercício de Laboratório 2
10 Primeiros múltiplos de 3
Autor: Lucien Constantino
"""

def is_multiple_of_three(number):
  return number % 3 == 0
  
number = 0
count = 10

while count > 0:
  number += 1
  if is_multiple_of_three(number):
    print(number)
    count -= 1

  

