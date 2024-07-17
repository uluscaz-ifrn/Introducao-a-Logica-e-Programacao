#Implemente um programa que calcule o valor do desconto de uma mercadoria. O programa deve ler
#e exibir o nome do produto, o valor e o percentual do desconto. Ao final deve exibir, além das
#informações iniciais, o valor do desconto e o valor a ser cobrado

nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual do desconto: "))
valor_desconto = (desconto / 100) * valor_produto
novo_valor_produto = valor_produto - valor_desconto
print("O nome do produto é %s, o valor do produto é %.2f reais, o desconto é de %.2f porcento e o valor a ser cobrado será %.2f"
    % (nome_produto, valor_produto, desconto, novo_valor_produto))
