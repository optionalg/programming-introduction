"""
Aula 8
Exercício de Laboratório 12
Conversor Decimal para Binário
Autor: Lucien Constantino
"""

def decimal_to_binary(decimal_number):
  
  decimal_number = int(decimal_number)
  quotient = 1
  binary_string = ""
  dividend = decimal_number
  
  while True:
    quotient = dividend // 2
    remainder = dividend % 2
    binary_string = str(remainder) + binary_string
    
    dividend = quotient
    
    if quotient <= 0:
      return int(binary_string)
  
assert decimal_to_binary(18) == 10010
assert decimal_to_binary(16) == 10000
assert decimal_to_binary(8) == 1000
assert decimal_to_binary(7) == 111
assert decimal_to_binary(1) == 1
assert decimal_to_binary(0) == 0

decimal_number = int(input("Digite um número em decimal: "))
print("{0} em binário é: {1}".format(decimal_number, decimal_to_binary(decimal_number)))


