"""
Aula 7
Laboratório
Exercício 6
Banco Imobiliário
Autor: Lucien Constantino
"""
# Banco Imobiliário

spot = input("Digite o nome da casa: ").upper()

if spot == "IMPOSTO":
	print("Se cair nesta casa o jogador deve pagar 10% de seus honorários")
elif spot == "TERRENO OU EMPRESA SEM DONO":
	print("Se cair num terreno ou empresa poderá comprá-las ao banqueiro, pagando o preço indicado no tabuleiro.")
elif spot == "PRISÃO":
	print("Se o jogador cair no campo \"VA PARA A CADEIA\" irá com o seu peão para a prisão. Se, porém, alcançar a prisão em lances regulares será considerado visitante")
elif spot == "TERRENO OU EMPRESA COM DONO":
	print("Se o jogador alcançar um terrno ou empresa que já tenha sido adquirido, pagará aluguel ou taxa.")

