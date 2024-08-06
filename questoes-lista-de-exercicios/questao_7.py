def pode_ser_triangulo(A, B, C):
    
    if A + B > C and A + C > B and B + C > A:
        return True
    else:
        return False

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if pode_ser_triangulo(A, B, C):
    print("Os valores podem ser os lados de um triângulo.")
else:
    print("Os valores não podem ser os lados de um triângulo.")


