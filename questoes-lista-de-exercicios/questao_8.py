A = float(input("Informe o valor do lado A: "))
B = float(input("Informe o valor do lado B: "))
C = float(input("Informe o valor do lado C: "))

def verificar_triangulo(A, B, C):
    if A + B > C and A + C > B and B + C > A:
        if A == B == C:
            return "Triângulo Equilátero"
        elif A == B or A == C or B == C:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não forma um triângulo"


tipo_triangulo = verificar_triangulo(A, B, C)
print("Os lados %2.f, %2.f e %2.f formam um %s." % (A, B, C, tipo_triangulo))
