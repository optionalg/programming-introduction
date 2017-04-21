"""
Aula 8
Exercício de Laboratório 13
Calculadora
Autor: Lucien Constantino
"""

def get_valid_operation():
  while True:
    
    operation = input("Operação: ")
    if (operation != "+" and 
    operation != "-" and 
    operation != "*" and 
    operation != "/" and 
    operation != "0"):
      print("Operação não disponível.")
    else:
      return operation

def operations(operation, a, b):
  
  a = float(a)
  b = float(b)
  
  if operation == "+":
    return a + b
  elif operation == "-":
    return a - b
  elif operation == "*":
    return a * b
  elif operation == "/":
    if b != 0:
      return a / b
    else:
      print("Não é possível dividir por 0.")
      
assert operations("+", 3, 4) == 7
assert operations("-", 3, 4) == -1
assert operations("*", 3, 4) == 12
assert operations("/", 3, 4) == 0.75

while True:
  
  operation = get_valid_operation()
  if operation == "0":
    break
  
  a = input("Digite o primeiro número: ")
  b = input("Digite o segundo número: ")
  result = operations(operation, a, b)
  if result != None:
    print("O resultado de {0} {1} {2} = {3}".format(a, operation, b, result))
