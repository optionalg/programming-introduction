# Jogo 2 Dados

import random

def rollDices():
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	return (dice1, dice2)

dices = rollDices()
result = dices[0] + dices[1]

bet = int(input("Digite sua aposta: "))
if bet < 1 or bet > 12:
	print("❌ Aposta inválida. Digite um valor entre 1 e 12.")
elif bet == result:
	print("🏆")
else:
	print("Errou! Resultado: {0}".format(result))

