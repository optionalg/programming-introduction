# Jogo Par ou Ímpar

import random

def betInput():
	print("Digite P para Par e I para Impar")
	bet = input("Você escolhe par ou ímpar? ")
	return bet

isBetEven = False

while True:
	bet = betInput()
	if (bet != 'P') and (bet != 'I'):
		print("Escolha uma opção válida.")
	else:
		isBetEven = bet == 'P'
		break

def numberInput():
	playerNumber = int(input("Quantos dedos você mostrou? "))
	return playerNumber

while True:
	playerNumber = numberInput()
	if playerNumber < 0 or playerNumber > 10:
		print("Mostre no mínimo 0, e no máximo 10 dedos.")
	else:
		break
		
computerNumber = random.randint(0, 10)
result = playerNumber + computerNumber
resultIsEven = result % 2 == 0

print("Maquina mostrou {0}".format(computerNumber))
if resultIsEven and isBetEven:
	print("🏆")
else:
	print("Você perdeu 🙁")

