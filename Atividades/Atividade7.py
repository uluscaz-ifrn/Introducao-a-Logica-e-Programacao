num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
operacao = input(
    "Digite a operação desejada: adição(+), subtração(-), multiplicação(*), divisão:(/) "
)
if operacao == "+":
  print("O resultado da soma é: ", num1 + num2)
elif operacao == "-":
  print("O resultado da subtração é: ", num1 - num2)
elif operacao == "*":
  print("O resultado da multiplicação é: ", num1 * num2)
elif operacao == "/":
  print("O resultado da divisão é: ", num1 / num2)
