"""
Aula 9
Exercícios Duplas 3
Média de notas das turmas
Autor: Lucien Constantino
"""

def get_grade(message):
    while True:
        grade = float(input(message))
        if grade < 0 or grade > 10:
            print("Nota inválida")
        else:
            return grade


classes = 3
students_per_class = 20

class_count = 0
student_count = 0

while class_count < classes:

    student_count = 0
    sum_of_grades = 0

    while student_count < students_per_class:

        prompt = "Digite a nota do aluno {0} da turma {1}: ".format(student_count + 1, class_count + 1)
        grade = get_grade(prompt)
        sum_of_grades += grade
        student_count += 1

    class_average = sum_of_grades / students_per_class
    print("Média da turma: {0:.1f}".format(class_average))

    class_count += 1
