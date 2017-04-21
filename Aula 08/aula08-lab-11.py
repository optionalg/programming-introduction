"""
Aula 8
Exercício de Laboratório 11
Conversor Binário > Decimal
Autor: Lucien Constantino
"""

import math

def binary_to_decimal(binary_number):
  
  binary_str = str(binary_number)
  positions = len(binary_str)
  count = 0
  sum = 0
  
  while count < positions:
    
    bit_position = positions - 1 - count
    bit = int(binary_str[bit_position])    
    sum += bit * math.pow(2, count)
    
    count += 1
  
  return int(sum)

assert binary_to_decimal(10010) == 18

num = input("Digite um número binário: ")
print("{0} em decimal = {1}".format(num, binary_to_decimal(num)))
