# 👊🖐️✌

import random
from enum import Enum

class Hand(Enum):
	Rock = 1
	Paper = 2
	Scissors = 3
	
class Winner(Enum):
	Draw = 0
	P1 = 1
	P2 = 2

print("Pedra = 👊\nPapel = ✋️\nTesoura = ✌️")

def bet(player):
	betString = input("Aposta do jogador {0}: ".format(player))
	if betString == "Pedra":
		return Hand.Rock
	elif betString == "Papel":
		return Hand.Paper
	elif betString == "Tesoura":
		return Hand.Scissors

p1 = bet("1")
p2 = bet("2")

def winner(p1, p2):
			
	winner = Winner.Draw
	
	if p1 == Hand.Rock:
		if p2 == Hand.Paper:
			winner = Winner.P2
		elif p2 == Hand.Scissors:
			winner = Winner.P1

	elif p1 == Hand.Paper:
		if p2 == Hand.Rock:
			winner = Winner.P1
		elif p2 == Hand.Scissors:
			winner = Winner.P2

	elif p1 == Hand.Scissors:
		if p2 == Hand.Rock:
			winner = Winner.P2
		elif p2 == Hand.Paper:
			winner = Winner.P1

	return winner
			
result = winner(p1, p2)
if result == Winner.Draw:
	print("Empate")
elif result == Winner.P1:
	print("Vitória jogador 1")
elif result == Winner.P2:
	print("Vitória jogador 2")

assert winner(Hand.Rock, Hand.Rock) == Winner.Draw
assert winner(Hand.Rock, Hand.Paper) == Winner.P2
assert winner(Hand.Rock, Hand.Scissors) == Winner.P1
assert winner(Hand.Paper, Hand.Rock) == Winner.P1
assert winner(Hand.Paper, Hand.Paper) == Winner.Draw
assert winner(Hand.Paper, Hand.Scissors) == Winner.P2
assert winner(Hand.Scissors, Hand.Rock) == Winner.P2
assert winner(Hand.Scissors, Hand.Paper) == Winner.P1
assert winner(Hand.Scissors, Hand.Scissors) == Winner.Draw

