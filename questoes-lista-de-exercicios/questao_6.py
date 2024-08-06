nota = float(input("Digite a nota: "))
nota2 = float(input("Digite a  segunda nota: "))
media = (nota + nota2) / 2
resultadofinal = ""
if media >= 7:
  resultadofinal = "Aprovado"
elif media < 3:
  resultadofinal = "Reprovado"
elif media >= 3 and media < 7:
  resultadofinal = "Quarta Prova"
print(resultadofinal)
