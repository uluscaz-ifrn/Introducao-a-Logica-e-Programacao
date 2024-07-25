n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
print(f"Os números informados são: {n1}, {n2}, {n3}")
if n1 < n2:
    n1, n2 = n2, n1
if n1 < n3:
    n1, n3 = n3, n1
if n2 < n3:
    n2, n3 = n3, n2
print(f"Os números em ordem decrescente são: {n1}, {n2}, {n3}")
