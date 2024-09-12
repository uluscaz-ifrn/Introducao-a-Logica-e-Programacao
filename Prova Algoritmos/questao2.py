#José Lucas da Silva Dantas
#Daniel Augusto Silva de Goés

n = int(input("Digite um número inteiro positivo: "))

a = 0 
b = 1

print(a)
print(b)

for _ in range(2, n):
   c = a+b
   a = b
   b = c
   print(c)