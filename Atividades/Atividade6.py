categoria = int(input("Informe a categoria do produto: "))
preco = 0
if categoria == 1:
  preco = 10
else:
  if categoria == 2:
    preco = 18
  else:
    if categoria == 3:
      preco = 23
    else:
      if categoria == 4:
        preco = 26
      else:
        if categoria == 5:
          preco = 31
print("O preço do produto é: R$", preco)
