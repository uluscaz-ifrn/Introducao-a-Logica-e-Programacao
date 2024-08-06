nota = float(input("Digite sua nota: "))
frenquencia = float(input("Digite sua frequência: "))
situacao = ""

if frenquencia < 75:
    situacao = "Reprovado"
elif frenquencia >= 75 and nota <= 3:
    situacao = "Reprovado"
elif frenquencia >= 75 and nota <= 7:
    situacao = "Quarta prova"
elif frenquencia >= 75 and nota > 7:
    situacao = "Aprovado"
print("Você obteve a nota %f e uma frequência de %f %s" %(nota, frenquencia, situacao))
