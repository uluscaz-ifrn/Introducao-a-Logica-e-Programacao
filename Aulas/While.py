    """"
    i = 0
    while i < 10:
      print(i)
      i = i + 1
    """ 
    total_geral = 0
    i = 1
    while i <= 3:
        qtd_acai = int(input("Digite a quantidade de açaís vendidos nos últimos %d dias: " %i))
        total = qtd_acai*3
        print("Total vendido: R$ %2.f de açaí" %total)
        total_geral = total_geral+total
        i = i + 1
    print("Foram vendidos R$ %2.f de açaí nos %d dias" %(total_geral, i))
