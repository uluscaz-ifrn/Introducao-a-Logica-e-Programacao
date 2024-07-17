#Faça um algoritmo para calcular a média aritmética entre dois valores fornecidos pelo usuário e exiba  o resultado.
"""""
valor1 = float(input("Digite o primeiro valor: "))
valor2 = valor1 = float(input("Digite o primeiro valor: "))
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
#Construa um programa que lê dois valores e os armazena em duas variáveis do tipo char, a variável A
#e a variável B. Utilize atribuições e quantas variáveis desejar para permutar os valores de A e B. O seu
#programa deve apresentar na tela o valor de A e o valor de B (espera-se que estejam trocados).
"""""
a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")
a_trocado = a
a = b
b = a_trocado
print(a, b)
""" ""

#Implemente um programa que calcule a bonificação por tempo de serviço de um funcionário. O
#usuário deve digitar quantos anos foram trabalhados e de quantos reais é a bonificação por ano
"""""

ano_trabalhado = int(input("Digite quantos anos foram trabalhados: "))
bonificacao_anual = float(
    input("Digite o valor de quantos reais é a bonificação por ano: "))
bonificacao_por_tempo_de_servico = ano_trabalhado * bonificacao_anual
print("Sua bonificação será de", bonificacao_por_tempo_de_servico)
""" ""

#Implemente um programa que calcule o valor do desconto de uma mercadoria. O programa deve ler
#e exibir o nome do produto, o valor e o percentual do desconto. Ao final deve exibir, além das
#informações iniciais, o valor do desconto e o valor a ser cobrado

valor_produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual do desconto: "))
valor_desconto = (desconto / 100) * valor_produto
novo_valor_produto = valor_produto - valor_desconto
print(
    "O valor do produto é %.2f reais, o desconto é de %.2f porcento e o valor a ser cobrado será %.2f"
    % (valor_produto, desconto, novo_valor_produto))
