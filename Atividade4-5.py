#Implemente um programa que calcule o valor do desconto de uma mercadoria. O programa deve ler
#e exibir o nome do produto, o valor e o percentual do desconto. Ao final deve exibir, além das
#informações iniciais, o valor do desconto e o valor a ser cobrado.

nome_produto = input("Informe o nome do produto: ")
valor_produto = float(input("Informe o valor do produto: "))
desconto = float(input("Digite o percentual do desconto: "))
valor_desconto = (desconto / 100) * valor_produto
novo_valor_produto = valor_produto - valor_desconto
print(
    f"O produto é {nome_produto}, o valor é R$ {valor_produto}, o desconto é de {valor_desconto} e o valor a ser cobrado é de R$ {novo_valor_produto}"
)

#Implemente um calculadora de IMC.

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso / (altura * altura)
print(f"O seu IMC é: {imc:.2f}")

