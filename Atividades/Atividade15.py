#Dado três valores, A, B e C, construa um algoritmo em Python para verificar se estes valores podem ser valores dos lados de um triângulo.

def triangulo(a, b, c):
  if (a > abs(b - c) and a < b + c) and \
     (b > abs(a - c) and b < a + c) and \
     (c > abs(a - b) and c < a + b):
    return "Os valores podem formar um triângulo."
  else:
    return "Os valores não podem formar um triângulo."


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

resultado = triangulo(a, b, c)

print(resultado)
