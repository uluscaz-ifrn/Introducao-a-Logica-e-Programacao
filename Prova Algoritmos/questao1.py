#José Lucas da Silva Dantas
#Daniel Augusto Silva de Goés

#A variável soma inicializa seu valor com 0. Essa variável será utilizada para acumular a soma dos números pares.
soma = 0

#O programa solicita ao usuário que digite um número inteiro positivo. 
n = int(input("Digite um número inteiro positivo: "))

#Verifica se o número digitado pelo usuário é menor que 0, caso seja, significa que o usuário digitou um número negativo
if n < 0:
  print("O número deve ser positivo.")
else:
  #Inicia um loop for onde a variável i assume valores de 1 até n
  for i in range(1, n + 1):
    #Verifica se o valor atual de i é par.
    if i % 2 == 0:
      #Se i for par, o seu valor é adicionado à variável soma
      soma += i
  print("A soma dos números pares de 1 até", n, "é:", soma)
