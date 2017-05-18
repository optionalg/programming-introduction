"""
Exercício 7
Autor: Lucien Constantino
"""

def get_answer(question):
    while True:
        answer: str = input("Resposta para a questão #{0}: ".format(question + 1))
        answer = answer.upper()

        if (answer != "A" and
                    answer != "B" and
                    answer != "C" and
                    answer != "D" and
                    answer != "E"):
            print("Resposta inválida")
        else:
            return answer


right_answers = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
number_of_right_answers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_students = 0
total_number_of_points = 0
proceed = True

while proceed:

    print("Aluno #{0}".format(number_of_students + 1))
    for i, right_answer in enumerate(right_answers):
        answer = get_answer(i)
        if answer == right_answer:
            number_of_right_answers[i] += 1
            total_number_of_points += 1

    number_of_students += 1

    stop_condition = input("Deseja colocar outro aluno? Digite 0 para terminar.")
    if stop_condition == "0":
        proceed = False

most_points = max(number_of_right_answers)
least_points = min(number_of_right_answers)
question_with_most_points = number_of_right_answers.index(most_points)
question_with_least_points = number_of_right_answers.index(least_points)

print("Questão com maior número de acertos: #{0}".format(question_with_most_points + 1))
print("Questão com menor número de acertos: #{0}".format(question_with_least_points + 1))
print("Média de notas da Turma: {0:.2f}".format(total_number_of_points / number_of_students))
