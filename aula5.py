#Construa um programa que lê dois valores e os armazena em duas variáveis do tipo char, a variável A
#e a variável B. Utilize atribuições e quantas variáveis desejar para permutar os valores de A e B. O seu
#programa deve apresentar na tela o valor de A e o valor de B (espera-se que estejam trocados).

a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")
a_trocado = a
a = b
b = a_trocado
print(a, b)
