"""
Aula 9
Exercícios Duplas 2
Formulário - Alunos Aprovados/Reprovados
Autor: Lucien Constantino
"""

def get_student_count():
    while True:
        student_count = int(input("Digite a quantidade de alunos para lançar notas: "))
        if student_count < 1 or student_count > 200:
            print("Número inválido de estudantes.")
        else:
            return student_count


def get_grade():
    while True:
        grade = float(input("Digite a nota: "))
        if grade < 0 or grade > 10:
            print("Nota inválida")
        else:
            return grade


student_count = get_student_count()
count = 0
cut_grade = 6.0
approved_students_count = 0

while count < student_count:

    print("Aluno {0}".format(count + 1))
    n1 = get_grade()
    n2 = get_grade()
    average = (n1 + n2) / 2
    print("Média: {0:.2f}".format(average))

    if average >= cut_grade:
        approved_students_count += 1
    count += 1

reproved_student_count = count - approved_students_count
print("Quantidade de alunos aprovados: {0}".format(approved_students_count))
print("Quantidade de alunos reprovados: {0}".format(reproved_student_count))
