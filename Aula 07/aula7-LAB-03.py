# Classificação Criminoso

questions = []
questions.append("Telefonou para a vítima?")
questions.append("Esteve no local do crime?")
questions.append("Mora perto da vítima?")
questions.append("Devia para a vítima?")
questions.append("Já trabalhou com a vítima?")

answerPoints = 0

for question in questions:
	print(question)
	isTrue = bool(input("Verdadeiro (True) ou Falso (False)?: "))
	if isTrue:
		answerPoints += 1


def classification(points):
	classification = "Inocente"
	if points == 2:
		classification = "Suspeita"
	elif points >= 3 and points <= 4:
		classification = "Cúmplice"
	elif points == 5:
		classification = "Assassino"
	return classification

print("Classificação: {0}".format(classification(answerPoints)))

assert classification(0) == "Inocente"
assert classification(1) == "Inocente"
assert classification(2) == "Suspeita"
assert classification(3) == "Cúmplice"
assert classification(4) == "Cúmplice"
assert classification(5) == "Assassino"
