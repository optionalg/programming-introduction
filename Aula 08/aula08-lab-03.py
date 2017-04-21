"""
Aula 8
Exercício de Laboratório 2
Média Semestreal
Autor: Lucien Constantino
"""

number_of_students = int(input("Número de alunos: "))
count = 0
sum_of_grades = 0

while count < number_of_students:

  print("------ Aluno {0} ------".format(count + 1))
  n1 = float(input("Nota P1: "))
  n2 = float(input("Nota P2: "))
  average = (n1 + n2) / 2
  sum_of_grades += average
  count += 1

class_average_grade = sum_of_grades / number_of_students
print("Nota média da turma: {0:.1f}".format(class_average_grade))
    
  
