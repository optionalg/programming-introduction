"""
Aula 9
Exercícios Tutoriados 1
Lê e valida nota
Autor: Lucien Constantino
"""

def get_nota():

    while True:
        nota = float(input("Digite a nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida")
        else:
            return nota

nota = get_nota()
print("Nota do aluno: {0:.1f}".format(nota))
