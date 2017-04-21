"""
Aula 7
Laboratório
Exercício 7
Jogo de Dados
Autor: Lucien Constantino
"""
from enum import Enum
import random

class Winner(Enum):
	noOne = 0
	player1 = 1
	player2 = 2
	draw = 3

def matchResult(player1Points, player2Points):
	winner = Winner.draw
		
	if player1Points < 10 and player2Points < 10:
		winner = Winner.noOne
	elif player1Points > player2Points:
		winner = Winner.player1
	elif player1Points < player2Points:
		winner = Winner.player2
	
	return winner

assert matchResult(1, 2) == Winner.noOne
assert matchResult(9, 9) == Winner.noOne
assert matchResult(10, 10) == Winner.draw
assert matchResult(20, 20) == Winner.draw
assert matchResult(30, 20) == Winner.player1
assert matchResult(20, 30) == Winner.player2

playerPoints = [0, 0]
rounds = 3

for round in range(rounds):
	for player in range(len(playerPoints)):
		input("Jogador {0} - Jogue o dado".format(player+1))
		diceResult = random.randint(1, 6)
		print("🎲 = " + str(diceResult))
		playerPoints[player] += diceResult
	
winner = matchResult(playerPoints[0], playerPoints[1])
if winner == Winner.player1:
	print("🏆 Jogador 1 (🔢 {1} ✖️ {2})".format(round, playerPoints[0], playerPoints[1]))
elif winner == Winner.player2:
	print("🏆 Jogador 2 (🔢 {1} ✖️ {2})".format(round, playerPoints[0], playerPoints[1]))
elif winner == Winner.draw:
	print("Empate".format(round))
elif winner == Winner.noOne:
	print("Ninguém ganhou! (🔢 {1} ✖️ {2})".format(round, playerPoints[0], playerPoints[1]))

