#Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação segundo a seguinte tabela:
#- maior de idade;
#- menor de idade;
#- pessoa idosa (idade superior ou igual a 65 anos).

idade = int(input("Digite sua idade: "))
if idade >= 65:
  print("Pessoa idosa")
elif idade >= 18:
  print("Maior de idade")
elif idade < 18:
  print("Menor de idade")
