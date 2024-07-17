#Faça um algoritmo para calcular a média aritmética entre dois valores fornecidos pelo usuário e exiba  o resultado.
"""""
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
media = (valor1+valor2)/2
print(media)
""" ""

#Construa um programa que calcula o novo salário de um funcionário. O usuário deverá informar o
#valor do salário e esse receberá um aumento de 15,8%. O programa deverá exibir o valor do salário
#recalculado.
"""""
salario = float(input("Digite o seu atual salario: "))
aumento = (15.8/100) * salario
novo_salario = salario + aumento
print("Seu novo salario e %.2f reais" % novo_salario")
""" ""
