a = 10
b = 20
new_a = a

a = b
b = new_a
print(a, b)

salario_atual = int(input("Digite seu salario: "))
aumento = float(input("Digite o aumento: "))
novo_salario = salario_atual + (salario_atual * aumento / 100)
print("Seu novo salario e %.2f reais" % novo_salario)

# 11/07/2024