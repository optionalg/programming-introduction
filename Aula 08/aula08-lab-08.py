"""
Aula 8
Exercício de Laboratório 8
Maior e menor números
Autor: Lucien Constantino
"""

count = 0
num = 1
biggest_number = 0
smallest_number = 0

while True:
    
  num = int(input("Digite um número: "))  
  if num < 0:
    break
  
  if num > biggest_number:
    biggest_number = num
  
  if count == 0:
    smallest_number = num
  
  if num < smallest_number:
    smallest_number = num
  
  count += 1

print("Maior número: {0}".format(biggest_number))
print("Menor número: {0}".format(smallest_number))

