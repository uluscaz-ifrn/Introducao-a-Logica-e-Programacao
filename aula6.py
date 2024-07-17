#Implemente um programa que calcule a bonificação por tempo de serviço de um funcionário. O
#usuário deve digitar quantos anos foram trabalhados e de quantos reais é a bonificação por ano

ano_trabalhado = int(input("Digite quantos anos foram trabalhados: "))
bonificacao_anual = float(
    input("Digite o valor de quantos reais é a bonificação por ano: "))
bonificacao_por_tempo_de_servico = ano_trabalhado * bonificacao_anual
print("Sua bonificação será de", bonificacao_por_tempo_de_servico)
