saldo_medio = float(input("Digite o saldo médio: "))
credito_especial = 0
if saldo_medio <= 500:
  credito_especial = 0
elif saldo_medio <= 1000:
  credito_especial = saldo_medio * 0.3
elif saldo_medio <= 3000:
  credito_especial = saldo_medio * 0.4
else:
  credito_especial = saldo_medio * 0.5
print(
    f"O saldo médio é {saldo_medio} e o valor do crédito liberado é {credito_especial}"
)
