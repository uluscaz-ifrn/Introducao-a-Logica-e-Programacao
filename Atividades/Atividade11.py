idade = int(input("Digite a idade: "))
classe_eleitoral = ""
if idade < 16:
  classe_eleitoral = "Não eleitor"
elif idade >= 18 and idade <= 65:
  classe_eleitoral = "Eleitor obrigatório"
elif idade >= 16 and idade <= 18 or idade > 65:
  classe_eleitoral = "Eleitor facultativo"
print(classe_eleitoral)
