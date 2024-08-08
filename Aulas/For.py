#for i in range(10):
#  print(i)
total_geral = 0

for i in range(1, 4):
  qts_acai = int(input("Digite a quantidade de açaís vendidos nos últimos %d atrás" %i))
  total = qts_acai * 3.00
  print("Total vendido: R$ %2.f de açaí" %total)
  total_geral = total_geral + total
print("Foram vendidos R$ %2.f de açaí nos últimos %d dias" %(total_geral, i))