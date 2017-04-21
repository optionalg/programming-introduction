# Jogo Extra - 5 Questões 

print("Responda as questões abaixo utilizando o número indicado (de 1 a 3).\n")

options = []
questions = []

q = "O que significa o acrônimo \"LOL\" quando é usado na internet ou mensagens de texto em celulares?"
a0 = "Laughing Out Loud"
a1 = "Little Old Lady"
a2 = "League of Legends"
options.append([a0, a1, a2])
questions.append(q)

q = "Em que ano o primeiro computador Apple foi lançado?"
a0 = "1970"
a1 = "1976"
a2 = "1980"
options.append([a0, a1, a2])
questions.append(q)

q = "Na barra de endereço de um navegador, o que significa \"www\"?"
a0 = "World Wide Web"
a1 = "Wai Wai World"
a2 = "Wild Wild West"
options.append([a0, a1, a2])
questions.append(q)

q = "Steve Jobs, Steve Wozniak e Ronald Wayne fundaram qual empresa?"
a0 = "Microsoft"
a1 = "Google"
a2 = "Apple"
options.append([a0, a1, a2])
questions.append(q)

q = "Em Ciência da Computação, qual o significado de \"GUI\"?"
a0 = "Graphical User Interface"
a1 = "Global Unique Identifier"
a2 = "Graphics Unit Interface"
options.append([a0, a1, a2])
questions.append(q)

correctAnswers = [0, 1, 0, 2, 0]
userAnswers = []

q = 0
for question in questions:

	print(question)	
	currentOptions = options[q]
	q = q + 1
	
	i = 0
	for option in currentOptions:
		i = i + 1
		print("{0}".format(i) + " - " + option)

	answer = int(input("Resposta: "))
	userAnswers.append(answer-1)
	
a = 0
points = 0
for userAnswer in userAnswers:
	if correctAnswers[a] == userAnswer:
		points = points + 1
	a = a + 1
	
print("Você acertou {0} de 5 questões".format(points))

