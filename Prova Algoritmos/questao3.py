#José Lucas da Silva Dantas
#Daniel Augusto Silva de Goés

i = 0
total_positivo = 0
total_negativo = 0

while i < 10:
  num = int(input("Digite um número inteiro: "))
  i += 1

  if num >= 1:
    total_positivo += 1
    print("O número é positivo.")
  elif num < 0:
    total_negativo += 1
    print("O número é negativo.")

print(f"Total de números positivos: {total_positivo}")
print(f"Total de numeros negativos: {total_negativo}")