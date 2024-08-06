nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (em porcentagem): "))

media = (nota1 + nota2) / 2

if frequencia < 75:
  situacao = "REPROVADO"
elif media < 3.0:
  situacao = "REPROVADO"
elif media >= 7.0:
  situacao = "APROVADO"
elif nota1 < 3.0 or nota2 < 3.0:
  situacao = "REPROVADO"
else:
  situacao = "QUARTA PROVA"

print("Situação do aluno:", situacao)
