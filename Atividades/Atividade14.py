#Dado três valores, A, B e C, construa um algoritmo em Python para verificar se estes valores podem ser valores dos
#lados de um triângulo, e se for, se é um triangulo escaleno, um triangulo equilátero ou um triangulo isósceles.


def verificar_triangulo(A, B, C):
    # Verifica a condição de existência de um triângulo
    if A + B > C and A + C > B and B + C > A:
        # Verifica o tipo de triângulo
        if A == B == C:
            return "Triângulo Equilátero"
        elif A == B or A == C or B == C:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não forma um triângulo"



A = float(input("Informe o valor do lado A: "))
B = float(input("Informe o valor do lado B: "))
C = float(input("Informe o valor do lado C: "))

tipo_triangulo = verificar_triangulo(A, B, C)
print(f"Os lados {A}, {B} e {C} formam um {tipo_triangulo}.")
