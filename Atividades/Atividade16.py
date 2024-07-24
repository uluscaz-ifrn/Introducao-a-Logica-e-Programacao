#Criar um algoritmo em Python que receba o valor de x, e calcule e imprima o valor de f(x)

x = float(input("Digite um valor para X: "))
fx = 0
if x <= 1:
    fx = 1
elif x > 1 and x <= 2:
    fx = 2
elif x > 2 and x <= 3:
    fx = x * x
elif x > 3:
    fx = x * x * x
print(f"O valor de f(x) é {fx}")
