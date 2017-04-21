"""
Aula 8
Exercício de Laboratório 15
Pesquisa de Satisfação
Autor: Lucien Constantino
"""

def get_gender():  
  while True:
    gender = input("Gênero (M ou F): ")
    if gender != "M" and gender != "F":
      print("Gênero inválido.")
    else:
      return gender
      
def get_opinion():
  while True:
    opinion = int(input("Qual sua opinião com relação ao produto: (1 a 5)"))
    if opinion < 1 and opinion > 5:
      print("Valor inválido.")
    else:
      return opinion
  
females_above_20_good = 0
females_above_30_bad = 0
men_awful = 0
men_count = 0
woman_count = 0
  
while True:
  age = input("Idade: ")
  if age == "s":
    break
  age = int(age)

  gender = get_gender()
  if gender == "M":
    men_count += 1
  else:
    woman_count += 1
  
  opinion = get_opinion()
  
  if gender == "F":
    if age > 20 and opinion == 4:
        females_above_20_good +=1
    if age > 30 and opinion == 2:
        females_above_30_bad +=1      
  if gender == "M" and opinion == 1:
    men_awful += 1

print("Quantidade de mulheres maiores de 20 anos que indicaram o produto como bom: {0}".format(females_above_20_good))
print("Quantidade de mulheres maiores de 30 anos que indicaram o produto como ruim: {0}".format(females_above_30_bad))
print("Quantidade de homens que indicaram o produto como péssimo: {0}".format(men_awful))
print("Total de mulheres que participaram da pesquisa: {0}".format(woman_count))
print("Total de homens que participaram da pesquisa: {0}".format(men_count))
