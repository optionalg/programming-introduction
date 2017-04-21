"""
Aula 9
Exercícios Tutoriados 2
Deseja continuar?
Autor: Lucien Constantino
"""

while True:
    command = input("Deseja continuar (s/n): ")
    if command == "s" or command == "n":
        break
    else:
        print("Não conheço este comando.")
