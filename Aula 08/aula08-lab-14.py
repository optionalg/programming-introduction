"""
Aula 8
Exercício de Laboratório 14
Pesquisa População
Autor: Lucien Constantino
"""

person_count = 0
oldest_age = 0
adult_females = 0

def is_adult(age):
  return age >= 18 and age <= 35

def get_gender():  
  while True:
    gender = input("Gênero (M ou F): ")
    if gender != "M" and gender != "F":
      print("Gênero inválido.")
    else:
      return gender
  
while True:  
  age = int(input("Idade: "))
  if age == -1:
    break
    
  person_count += 1
    
  if age > oldest_age:
    oldest_age = age
    
  gender = get_gender()
  if gender == "F" and is_adult(age):
    adult_females += 1

print("Maior idade: {0}".format(oldest_age))
adult_females_percent = (adult_females / person_count) * 100
print("Percentual de indivíduos do sexo feminino com idade entre 18 e 35 anos: {0:.1f}%".format(adult_females_percent))

