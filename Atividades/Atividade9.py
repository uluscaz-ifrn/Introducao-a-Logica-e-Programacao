saldo_medio = float(input("Digite o saldo médio: "))
credito_especial = ""

if saldo_medio <= 500:
  credito_especial = f"Nenhum crédito para {saldo_medio}"
elif saldo_medio > 501 and saldo_medio <= 1000:
  credito_especial = f"Saldo médio: {saldo_medio} crédito especial: {saldo_medio*30/100}"
elif saldo_medio > 1001 and saldo_medio <= 3000:
  credito_especial = f"Saldo médio: {saldo_medio} crédito especial: {saldo_medio*40/100}"
elif saldo_medio >= 3001:
  credito_especial = f"Saldo médio: {saldo_medio} crédito especial: {saldo_medio*50/100}"
print(credito_especial)
